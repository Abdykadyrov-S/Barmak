from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView, OAuth2CallbackView
from allauth.socialaccount.models import SocialAccount
from allauth.account.utils import perform_login
import uuid

class CustomGoogleOAuth2Adapter(GoogleOAuth2Adapter):
    def sociallogin_signup(self, request, sociallogin):
        user = sociallogin.user
        if not user.username:
            # Если у пользователя нет username, присвоим ему значение UUID
            user.username = str(uuid.uuid4())[:30]  # Предельная длина username
            user.save()
        # Продолжаем стандартный процесс регистрации
        return super(CustomGoogleOAuth2Adapter, self).sociallogin_signup(request, sociallogin)

oauth2_login = OAuth2LoginView.adapter_view(CustomGoogleOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(CustomGoogleOAuth2Adapter)