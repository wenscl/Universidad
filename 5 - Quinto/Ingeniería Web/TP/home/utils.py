from datetime import datetime, timezone, timedelta
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags
import hashlib

# Cantidad de posts por página.
POST_PER_PAGE = 10

# Generar clave de activación de cuenta.
def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()

# Configuración del envío de mails.
def send_email(subject, recipient_list, template, data):
    html_content = render_to_string(template, data)
    plain_text_content = strip_tags(html_content)

    send_mail(subject=subject,
              message=plain_text_content,
              html_message=html_content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=recipient_list)

# Enviar mail de confirmacion al usuario.
def send_activation_mail(user):
    # Generar clave de activacion y fecha de expiracion de la misma (1 dia).
    activation_key = generate_activation_key(user.username)
    user.activation_key = activation_key
    user.key_expiration_date = datetime.now(timezone.utc) + timedelta(days=1)

    user.save()

    send_email('Activa tu cuenta de The Movies of Our Lives!', [user.email], 'home/activation_email_template.html', {'token': activation_key,
                                                                                                                     'domain': settings.DOMAIN_URL })

# Enviar mail de aviso de baneo.
def send_ban_mail(user, type_ban, content):
    send_email('Aviso de baneo', [user.email], 'moderation/ban_email_template.html', { 'user': user.username,
                                                                                       'type_ban': type_ban,
                                                                                       'end_ban': user.temporary_ban_end_date,
                                                                                       'content': content })

# Enviar mail de aviso de cancelación de baneo.
def send_cancel_user_ban_mail(user):
    send_email('Aviso de cancelación de baneo', [user.email], 'moderation/cancel_user_ban_email_template.html', { 'user': user.username, })

# Paginar el contenido.
def paginate(content_list, page):
    paginator = Paginator(content_list, POST_PER_PAGE)

    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)