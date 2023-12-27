def serialize_user(user):
    return {
        "id": user.pk,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "is_admin": user.is_superuser
    }


def serialize_users(users):
    return [
        serialize_user(user) for user in users
    ]
