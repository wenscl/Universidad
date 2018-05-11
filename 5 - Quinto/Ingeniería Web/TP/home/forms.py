from .models import CustomUser
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import PasswordInput, TextInput, ValidationError, DateInput, DateField, ImageField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(min_length=8,
                                required=True,
                                widget=PasswordInput(attrs={'class': 'form-control'}),
                                label='Contraseña',
                                error_messages={'min_length': 'La contraseña debe tener, al menos, 8 caracteres.'})

    password2 = forms.CharField(min_length=8,
                                required=True,
                                widget=PasswordInput(attrs={'class': 'form-control'}),
                                label='Confirmar Contraseña',
                                error_messages={'min_length': 'La contraseña debe tener, al menos, 8 caracteres.'})

    class Meta:
        model = CustomUser
        fields = ['username','email', 'is_admin']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
            'is_admin': 'Es administrador',
        }

        error_messages = {
            'username': {
                'required': 'Debe ingresar un nombre de usuario.',
            },
            'email': {
                'invalid': 'Ingrese una dirección de correo válida.',
            }
        }

    def clean_password2(self):
        # Comprobar que las contraseñas coincidan.
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2

    def save(self, commit=True):
        # Guardar la contraseña suministrada hasheada.
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.state = CustomUser.UserProfileState.CONFIRMED.value
        if commit:
            user.save()
        return user

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
        }

        error_messages = {
            'username': {
                'required': 'Debe ingresar un nombre de usuario.',
            },
            'email': {
                'invalid': 'Ingrese una dirección de correo válida.',
            }
        }

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label='Contraseña',
        help_text='El sistema no almacena las contraseñas originales por lo cual no es posible visualizar la contraseña de este usuario, pero puede modificarla usando <a href="../password/">este formulario</a>.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'is_admin')

        labels = {
            'is_admin': 'Es administrador',
        }

    def clean_password(self):
        return self.initial['password']

class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=TextInput(attrs={'class': 'form-control'}),
                               label='Nombre de Usuario',
                               error_messages={'required': 'El campo \'Nombre de Usuario\' es requerido.'})
    password = forms.CharField(required=True,
                               widget=PasswordInput(attrs={'class': 'form-control'}),
                               label='Contraseña',
                               error_messages={'required': 'El campo \'Contraseña\' es requerido.'})

class EditProfileForm(forms.ModelForm):
    password1 = forms.CharField(min_length=8,
                                required=False,
                                widget=PasswordInput(attrs={'class': 'form-control'}),
                                label='Nueva Contraseña',
                                error_messages={'min_length': 'La contraseña debe tener, al menos, 8 caracteres.'},
                                help_text='Si no querés modificar tu contraseña, dejá este campo en blanco.')

    password2 = forms.CharField(min_length=8,
                                required=False,
                                widget=PasswordInput(attrs={'class': 'form-control'}),
                                label='Confirmar Nueva Contraseña',
                                error_messages={'min_length': 'La contraseña debe tener, al menos, 8 caracteres.'},
                                help_text='Si no querés modificar tu contraseña, dejá este campo en blanco.')

    date_of_birth = DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y'],
                              required=False,
                              label='Fecha de Nacimiento',
                              widget=DateInput(attrs={'class': 'form-control datepicker'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'first_name', 'last_name', 'password1', 'password2', 'profile_image')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
        }

        error_messages = {
            'username': {
                'required': 'Debe ingresar un nombre de usuario.',
            },
            'email': {
                'invalid': 'Ingrese una dirección de correo válida.',
            }
        }

    def clean_password2(self):
        # Comprobar que las contraseñas coincidan.
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        return password2

    def save(self, commit=True):
        # Guardar la contraseña suministrada hasheada.
        user = super(EditProfileForm, self).save(commit=False)
        if self.cleaned_data['password1']:
            user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class ComplaintForm(forms.Form):
    content_id = forms.IntegerField(widget=forms.HiddenInput(),
                                    required=True)

    comment = forms.CharField(max_length=500,
                              min_length=10,
                              label='Comentario',
                              help_text='Este campo es requerido. Necesitamos que ingreses un comentario explicando la razón de la denuncia (mínimo 10 caracteres).',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Explicanos el motivo de tu denuncia...'}),
                              required=True)