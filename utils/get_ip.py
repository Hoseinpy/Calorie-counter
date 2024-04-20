from django.contrib.auth.models import User


def get_user_ip(request):
    user_ip = request.META.get('REMOTE_ADDR')

    return user_ip