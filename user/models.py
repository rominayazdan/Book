from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models



class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class AllObjectsUsersManager(UserManager):
    def get_queryset(self):
        return super().get_queryset()








class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    national_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    objects = CustomUserManager()
    All_Objects= AllObjectsUsersManager()

    class Meta:
        permissions = (
            ("can_view_deleted_user", "Can view deleted users"),
            ("can_edit", "Can edit users"),
        )









