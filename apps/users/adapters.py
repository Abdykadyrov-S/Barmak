from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class NoSocialAccountConfirmationAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        This method can be overridden to perform extra checks, for example
        to see if the social account has been banned. In case of a ban,
        you can raise an ImmediateHttpResponse to abort the login.

        This example bypasses the signup form that typically asks for
        extra information (like user type).
        """
        # Skip the account signup form.
        if not sociallogin.is_existing:
            sociallogin.save(request, connect=True)
