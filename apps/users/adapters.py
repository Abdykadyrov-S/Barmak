from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login
from allauth.socialaccount.helpers import complete_social_login
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # Если пользователь уже существует, завершаем процесс входа
        if sociallogin.is_existing:
            perform_login(request, sociallogin.user, 'none')
            raise ImmediateHttpResponse(redirect('redirect_url_name'))
        # Если пользователь новый, создаем учетную запись и завершаем процесс входа
        user = sociallogin.user
        user.set_unusable_password()
        sociallogin.save(request)
        complete_social_login(request, sociallogin)
        raise ImmediateHttpResponse(redirect('redirect_url_name'))