from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ChangePasswordSerializer

class UserView(APIView):

    def post(self, request):
        action = request.query_params.get('action')

        if action == 'register':
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

        elif action == 'login':
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data['user']
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                })
            return Response({'detail': 'Invalid credentials'}, status=401)

        elif action == 'change-password':
            if not request.user.is_authenticated:
                return Response({"detail": 'Authentication required.'}, status=401)

            serializer = ChangePasswordSerializer(data=request.data)
            if serializer.is_valid():
                if not request.user.check_password(serializer.validated_data['old_password']):
                    return Response({'old_password': 'Wrong password.'}, status=400)
                if serializer.validated_data['old_password'] == serializer.validated_data['new_password']:
                    return Response({'detail': 'Please enter a different password!'}, status=400)

                request.user.set_password(serializer.validated_data['new_password'])
                request.user.save()
                return Response({'detail': 'Password updated.'})
            return Response(serializer.errors, status=400)

        return Response({'detail': 'Invalid action'}, status=400)

    def get(self, request):
        action = request.query_params.get('action')

        if action == 'list-users':
            if not request.user.is_authenticated or request.user.role != 'administrator':
                return Response({'detail': 'Admin only.'}, status=403)
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=401)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=401)
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)