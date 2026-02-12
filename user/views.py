from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from user.serializers import RegisterUserSerializer


# Create your views here.
class RegisterUserAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result" : {"user_id" : user.id}})

class ViewUserAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format = None):
        content ={
            'status' : 'request was permitted',
        }
        return Response(content)




