from django.core import exceptions
from django.http import JsonResponse
from django.views import View
import json
from .models import Book, Borrow
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class BooksView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = json.loads(request.body)
            book = Book(**data)
            book.save()
            book = Book.serialize(book)
        except:
            return JsonResponse({"error": "cannot create a new book"}, status=404)
        return JsonResponse(book, status=201)

    def get(self, request):
        try:
            books = Book.objects.all()
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Books not found'}, status=404)
        books = Book.serialize_lst(books)
        return JsonResponse(books, status=200, safe=False)


class BooksModifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404, safe=False)
        book = Book.serialize(book)
        return JsonResponse(book, status=200)

    def patch(self, request, pk):
        try:
            book = Book.objects.filter(pk=pk)
            if not book:
                raise exceptions.EmptyResultSet(f"Unable to find book {pk}")
            data = json.loads(request.body)
            book.update(**data)
        except exceptions.FieldDoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        except exceptions.EmptyResultSet as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        return JsonResponse({"data": f"Book {pk} changed."}, status=203,)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        return JsonResponse({"data": f"Book {pk} deleted."})


class BorrowBooks(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(pk=data["user"])
            book = Book.objects.get(pk=data["book"])
            if book.available_copies == 0:
                raise Exception("No copies left.")
            borrowed_users = User.objects.filter(book__title=book.title)
            if borrowed_users.contains(user):
                raise Exception("You cannot own the same book twice.")
            borrow = Borrow(user=user, book=book)
            borrow.save()
            book.available_copies -= 1
            book.save()
        except Exception as e:
            return JsonResponse({"error": f'{e}'}, status=404)
        return JsonResponse({"data": "Book borrowed successfully"}, status=201)

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            borrowed_books = Book.objects.filter(borrowers=user)
        except User.DoesNotExist as e:
            return JsonResponse({'error': 'User not found'}, status=404)
        borrowed_books = Book.serialize_lst(borrowed_books)
        return JsonResponse(borrowed_books, status=200, safe=False)

    def delete(self, request):
        try:
            user = User.objects.get(pk=request.GET.get('user'))
            book = Book.objects.get(pk=request.GET.get('book'))
            borrowed_record = Borrow.objects.filter(user=user, book=book)
            if not borrowed_record:
                raise Exception("You did not borrow this book")
            borrowed_record.delete()
            book.available_copies += 1
            book.save()
        except Exception as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        return JsonResponse({"data": "book returned."}, status=200)
