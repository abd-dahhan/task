from rest_framework import generics, permissions
from .models import Resume
from .serializers import ResumeSerializer


class ResumeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer