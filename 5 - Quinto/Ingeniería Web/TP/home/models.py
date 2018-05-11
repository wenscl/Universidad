from datetime import datetime, timedelta, timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.shortcuts import get_object_or_404
from enum import Enum

DAYS_OF_TEMPORARY_BAN = 3

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener un email.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser):
    class UserProfileState(Enum):
        CONFIRMATION_PENDING = 'Pendiente de Confirmación'
        CONFIRMED = 'Confirmado'
        TEMPORARILY_BANNED = 'Baneado Temporalmente'
        PERMANENTLY_BANNED = 'Baneado Permanentemente'

    username = models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo electrónico', max_length=100, unique=True)
    state = models.CharField(max_length=100,
                             verbose_name='Estado',
                             default=UserProfileState.CONFIRMED.value,
                             # Se definen los valores que puede tomar el campo 'Estado'.
                             choices=[(member.value, member.value) for name, member in UserProfileState.__members__.items()])
    temporary_ban_end_date = models.DateTimeField(verbose_name='Fecha de fin de baneo temporal', blank=True, null=True)
    activation_key = models.CharField(max_length=500, null=True, blank=True)
    key_expiration_date = models.DateTimeField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='Fecha de registro', auto_now_add=True)
    date_of_birth = models.DateTimeField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    profile_image = models.ImageField(verbose_name='Foto de perfil', upload_to = 'profile_images/', blank=True ,null=True)
    complaints = models.ManyToManyField('content.Content', related_name='complaints', through='Complaint')
    ban_count = models.IntegerField(verbose_name='Cantidad de baneos', default=0)
    favorite_content = models.ManyToManyField('content.Content', related_name='favorites', through='FavoriteContent')


    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Setear el baneo sobre el usuario. Si days es igual a 0, no se lo banea. Si days es -1, significa que el baneo es permanente.
    def set_ban(self, days):
        if days != 0:
            if days > 0:
                self.state = self.UserProfileState.TEMPORARILY_BANNED.value
                self.temporary_ban_end_date = datetime.now(timezone.utc) + timedelta(days=days)
            elif days == -1:
                self.state = self.UserProfileState.PERMANENTLY_BANNED.value

            self.ban_count += 1
            self.save()

    @property
    def is_confirmed(self):
        return self.state == self.UserProfileState.CONFIRMED.value

    @property
    def is_confirmation_pending(self):
        return self.state == self.UserProfileState.CONFIRMATION_PENDING.value

    @property
    def is_banned(self):
        return self.state in (self.UserProfileState.PERMANENTLY_BANNED.value, self.UserProfileState.TEMPORARILY_BANNED.value)

    @property
    def is_temporarily_banned(self):
        return self.state == self.UserProfileState.TEMPORARILY_BANNED.value

    @property
    def is_permanently_banned(self):
        return self.state == self.UserProfileState.PERMANENTLY_BANNED.value

    @property
    def is_staff(self):
        return self.is_admin

    @staticmethod
    def get_user(id):
        return get_object_or_404(CustomUser, id=id)

    @staticmethod
    def get_user_token(token):
        return get_object_or_404(CustomUser, activation_key=token)

    @staticmethod
    def ban_check(user):
        return user.is_confirmed

    @staticmethod
    def get_banned_users_list():
        return CustomUser.objects.filter(state__in=[CustomUser.UserProfileState.PERMANENTLY_BANNED.value, CustomUser.UserProfileState.TEMPORARILY_BANNED.value])

    def get_favorites_list(self):
        return [favorite.content for favorite in self.favoritecontent_set.filter(content__elimination_date__isnull=True,
                                                                                 content__reported=False).order_by('-date')]

    def add_to_favorites(self, content):
        self.favoritecontent_set.create(user=self, content=content)

    def remove_from_favorites(self, content):
        if self.favoritecontent_set.filter(content=content).exists():
            self.favoritecontent_set.get(content=content).delete()

    def add_complaint(self, content, comment):
        self.complaint_set.create(user=self,
                                  content=content,
                                  comment=comment)

    def __str__(self):
        return self.username


class Complaint(models.Model):
    content = models.ForeignKey('content.Content')
    user = models.ForeignKey(CustomUser)
    comment = models.CharField(max_length=500, verbose_name='Comentario')

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.comment)

class FavoriteContent(models.Model):
    user = models.ForeignKey(CustomUser)
    content = models.ForeignKey('content.Content')
    date = models.DateTimeField(verbose_name='Fecha', auto_now=True)

    class Meta:
        verbose_name = 'Contenido Favorito'
        verbose_name_plural = 'Contenidos Favoritos'