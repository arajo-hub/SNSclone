from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model

User=get_user_model() # user모델은 auth에 있는 User를 이용

class Post(models.Model):
    user=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField(max_length=256)
    message_html=models.TextField(editable=False)
    group=models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message # message를 Post를 대표하는 문자형로 함

    def save(self, *args, **kwargs):
        self.message_html=self.message
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering=['-created_at']
        unique_together=['user', 'message']
