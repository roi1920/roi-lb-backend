import json
from django.core import exceptions
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from books.models import Book
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from royLibraryBackend.serializers import serialize_user, serialize_users


class UsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            users = User.objects.all()
            if not users:
                raise Exception("No users in the database.")
        except Exception as e:
            return JsonResponse({'error': f"{e}"}, status=404)
        users = serialize_users(users)
        return JsonResponse(users, status=200, safe=False)


class UsersModifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404, safe=False)
        user = serialize_user(user)
        return JsonResponse(user, status=200)

    def patch(self, request, pk):
        try:
            user = User.objects.filter(pk=pk)
            if not user:
                raise exceptions.EmptyResultSet(f"Unable to find user {pk}")
            data = json.loads(request.body)
            user.update(**data)
        except exceptions.FieldDoesNotExist as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        except exceptions.EmptyResultSet as e:
            return JsonResponse({'error': f'{e}'}, status=404)
        return JsonResponse({"data": f"User {pk} changed."}, status=203,)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        return JsonResponse({"data": f"User {pk} deleted."})

class UserAdminToggle(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.is_superuser = not user.is_superuser
            user.save()
        except User.DoesNotExist as e:
            return JsonResponse({'error': 'User not found'}, status=404)
        return JsonResponse({"data": "user toggled."})
