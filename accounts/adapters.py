from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from rest_framework_simplejwt.tokens import RefreshToken

class SocialAdapter(DefaultSocialAccountAdapter):
    
   def pre_social_login(self, request, sociallogin):
        user = sociallogin.user

        if user.pk is None:
            user.save()
            
        refresh = RefreshToken.for_user(user)
        request.session["jwt_tokens"] = {
            "access":str(refresh.access_token),
            "refresh":str(refresh)
        }