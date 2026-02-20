from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer, CustomTokenSerializer, LogoutSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"user created"})
        return Response(serializer.errors,status=400)
    
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user =request.user
    return Response({
        "username":user.username,
        "email":user.email,
        "id":user.id
    })

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"msg":"logout successfull."})
    

# class GoogleLoginSuccessView(APIView):

#     # def get(self,request):
#     #     tokens = request.session.get("jwt_tokens")

#     #     if not tokens:
#     #         return Response({"error":"Tokens are not found"},status=400)
#     #     return Response(tokens)
    

#     def get(self,request):
        
#         # access = request.GET.get("access")
#         # refresh = request.GET.get("refresh")

#         # if not access:
#         #     return Response({"error":"tokens are not found"},status=400)

#         # return Response({
#         #     "access":access,
#         #     "refresh":refresh
#         # })
#         return Response({"msg":"login successfull"})




class GoogleLoginSuccessView(APIView):
    def get(self, request):

        access = request.session.get("access")
        refresh = request.session.get("refresh")

        if not access:
            return Response({"error": "tokens not found"}, status=400)

        return Response({
            "access": access,
            "refresh": refresh
        })