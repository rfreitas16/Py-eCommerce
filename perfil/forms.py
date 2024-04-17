from django import forms
from . import models
from django.contrib.auth.models import User


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fiedls = '__all__'
        exclude = ('usuario',)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha',
    )
    # validacao da senha
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmar senha'
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password', 'password2', 'email')

        def clean(self, *args, **kwargs):
            data = self.data
            cleaned = self.cleaned_data
            validation_error_msgs = {}

            # verificar o usuario e a senha
            usuario_data = cleaned.get('username')
            password_data = cleaned.get('password')
            password2_data = cleaned.get('password2')
            email_data = cleaned.get('email')

            error_msg_user_exists = 'Usuario ja existe'
            error_msg_email_exists = 'email ja existe'
            error_msg_password_match = 'As duas ferem nao conferem'
            error_msg_password_short = 'Sua senha deve ter pelo menos 6 caracteres'
            error_msg_requerid_field = 'Este campo e obrigatorio'

            usuario_db = User.objects.filter(usuario=usuario_data).first()
            email_db = User.objects.filter(email=email_data).first()

            # validar formulario
            # usuario logado atualizacao
            if self.usuario:
                if usuario_db:
                    if usuario_data != usuario_db.username:
                        validation_error_msgs['username'] = error_msg_user_exists

                    if email_db:
                        if email_data != email_db.email:
                            validation_error_msgs['email'] = error_msg_email_exists
                    if password_data:
                        if password_data != password2_data:
                            validation_error_msgs['password'] = error_msg_password_match
                            validation_error_msgs['password2'] = error_msg_password_match
                        if len(password_data) <6:
                            validation_error_msgs['password'] = error_msg_password_short
            else:
                    if usuario_db:
                        validation_error_msgs['username'] = error_msg_user_exists
                    if email_db:
                        validation_error_msgs['email'] = error_msg_email_exists

                    if not password_data:
                        validation_error_msgs['password'] = error_msg_requerid_field
                            
                    if not password2_data:
                        validation_error_msgs['password2'] = error_msg_requerid_field

                    if password_data != password2_data:
                            validation_error_msgs['password'] = error_msg_password_match
                            validation_error_msgs['password2'] = error_msg_password_match
                    if len(password_data) <6:
                            validation_error_msgs['password'] = error_msg_password_short

                    if validation_error_msgs:
                             raise (forms.ValidationError(validation_error_msgs))
