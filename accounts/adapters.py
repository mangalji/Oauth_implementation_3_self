from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect


# class AccountAdapter(DefaultAccountAdapter):

#     def get_login_redirect_url(self, request):
#         user = request.user

#         refresh = RefreshToken.for_user(user)
#         response = redirect("http://127.0.0.1:8000/api/google/success/")
        
#         response.set_cookie(
#             "access",str(refresh.access_token),httponly=True,secure=False,samesite="Lax"
#         )
#         response.set_cookie(
#             "refresh",str(refresh),httponly=True,secure=False,samesite="Lax"
#         )

#         # return f"http://127.0.0.1:8000/api/google/success/?access={refresh.access_token}&refresh={refresh}"
#         return response

class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):

        user = request.user
        refresh = RefreshToken.for_user(user)

        request.session["access"] = str(refresh.access_token)
        request.session["refresh"] = str(refresh)

        return "http://127.0.0.1:8000/api/google/success/"

class SocialAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get("email")

        if email:
            from django.contrib.auth import get_user_model
            User = get_user_model()

            try:
                user = User.objects.get(email=email)
                sociallogin.connect(request, user)
            except User.DoesNotExist:
                pass
































# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import get_user_model
# from django.shortcuts import redirect

# User = get_user_model()

# class SocialAdapter(DefaultSocialAccountAdapter):
    
# #     def pre_social_login(self, request, sociallogin):
# #         # user = sociallogin.user
# #         email = sociallogin.account.extra_data.get("email")

# #         if not email:
# #             return 
        
# #         try: 
# #             existing_user = User.objects.get(email=email)
# #             sociallogin.connect(request,existing_user)

# #         except User.DoesNotExist:
# #             pass

# #     def login(self,request,user):
# #         super().login(request,user)
# #         print("ADAPTER LOGIN RUNNING")
# #         # if user.pk is None:
# #         #     user.save()
# #         # refresh = RefreshToken.for_user(user)
# #         try:
# #             refresh = RefreshToken.for_user(user)
# #         except Exception as e:
# #             print(e)
# #         # request.session["jwt_tokens"] = {
# #         #     "access":str(refresh.access_token),
# #         #     "refresh":str(refresh)
# #         # }
# #         access = str(refresh.access_token)
# #         refresh = str(refresh)
# #         return redirect(
# #             f"http://127.0.0.1:8000/api/google/success/?access={access}&refresh={refresh}"
# #         )
#     # def login(self,request,user):
#     def get_login_redirect_url(self, request):
#         # return super().get_connect_redirect_url(request, socialaccount)
#         # super().login(request.user)
#         user = request.user
#         refresh = RefreshToken.for_user(user)
#         access = str(refresh.access_token)
#         refresh = str(refresh)

#         return redirect(
#             f"http://127.0.0.1:8000/api/google/success/?access={access}&refresh={refresh}"
#         )


# """
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class SocialAdapter(DefaultSocialAccountAdapter):

#     def pre_social_login(self, request, sociallogin):
#         email = sociallogin.account.extra_data.get("email")

#         if email:
#             try:
#                 user = User.objects.get(email=email)
#                 sociallogin.connect(request, user)
#             except User.DoesNotExist:
#                 pass"""