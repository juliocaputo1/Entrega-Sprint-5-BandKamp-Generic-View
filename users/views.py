from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@extend_schema(methods=["PUT"], exclude=True)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()