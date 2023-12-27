# from datetime import datetime
from django.db import models


# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=30)
#     is_admin = models.BooleanField(default=False)
#     date_of_birth = models.DateTimeField(default=datetime.now(), blank=True)

#     def serialize(user):
#         return {
#             "id": user.pk,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "email": user.email,
#             "is_admin": user.is_admin,
#             "date_of_birth": user.date_of_birth,
#         }

#     def serialize_lst(users):
#         return [
#             {
#                 "id": user.pk,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "email": user.email,
#                 "is_admin": user.is_admin,
#                 "date_of_birth": user.date_of_birth,
#             } for user in users
#         ]
