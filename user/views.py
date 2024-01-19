from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def user_registration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success', 'message': 'User registered successfully'})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        if not user or not user.is_active:
            return Response({'status': 'failed', 'message': 'Incorrect Credentials'}, status=400)
        access_token = RefreshToken.for_user(user)
        return Response(
            {'status': 'success', 'message': 'User logged in successfully',
             'access_token': str(access_token.access_token),
             'refresh_token': str(access_token)}
        )
    return Response(serializer.errors, status=400)
