from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, full_name, password):
        if not email:
            raise ValueError('you must have email')
        if not username:
            raise ValueError('you must have username')
        if not full_name:
            raise ValueError('you must have fullname')
        if not phone_number:
            raise ValueError('you nust enter phone number')

        user = self.model(username=username, email=self.normalize_email(
            email), phone_number=phone_number, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, full_name, password):
        user = self.create_user(
            username, email,  phone_number, full_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
