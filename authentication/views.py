from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from authentication.serializer import UserSerializer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset