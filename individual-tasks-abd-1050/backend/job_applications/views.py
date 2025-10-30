from rest_framework import generics, permissions
from .models import Resume
from .serializers import ResumeSerializer
from django.core.mail import send_mail
from django.conf import settings

class ResumeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


    def perform_create(self, serializer):
        resume = serializer.save()
        
        subject = f'New Resume Created: {resume.name}'
        message = (
            f'A new resume has been created.\n\n'
            f'Name: {resume.name}\n'
            f'Bio: {resume.bio}\n'
            f'Address: {resume.address}\n'
        )

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )