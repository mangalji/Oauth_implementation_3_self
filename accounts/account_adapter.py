from allauth.account.adapter import DefaultAccountAdapter
from rest_framework_simplejwt.tokens import RefreshToken

class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        print("account adapter running.")

        user = request.user

        refresh = RefreshToken.for_user(user)

        access = str(refresh.access_token)
        refresh = str(refresh)

        return f"http://127.0.0.1:8000/api/google/success/?access={access}&refresh={refresh}"