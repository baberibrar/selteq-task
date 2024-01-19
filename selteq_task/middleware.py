from django.contrib.auth.models import User
from django.http import JsonResponse
import jwt
from selteq_task.settings import SECRET_KEY
from django.utils.functional import SimpleLazyObject

secret_key = SECRET_KEY

allowed_paths = ['/user/login/', '/user/registration/', '/admin/login/']
secure_paths = ['/tasks/']


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow superuser to access any endpoint
        if request.user.is_superuser:
            return self.get_response(request)

        # Allow access to certain paths without authentication
        if request.path in allowed_paths:
            return self.get_response(request)

        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return JsonResponse({'error': 'Authorization header is missing'}, status=401)

        try:
            token = authorization_header.split(' ')[1]
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])

            user = User.objects.get(id=payload['user_id'])

            if user is not None:
                request.user = SimpleLazyObject(lambda: user)
            else:
                return JsonResponse({'error': 'User authentication failed'}, status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=401)

        return self.get_response(request)
