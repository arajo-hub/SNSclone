from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

User=get_user_model()

from django import template
register=template.Library() # register는 유효한 태그 라이브러리를 만들기 위한 모듈레벨의 인스턴스 객체

class Group(models.Model):
    name=models.CharField(max_length=255, unique=True)
    slug=models.SlugField(allow_unicode=True, unique=True)
    description=models.TextField(blank=True, default='')
    description_html=models.TextField(editable=False, default='', blank=True)
    members=models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name) # Group name을 slug화해준다. 예를 들어, b b b라면 b-b-b
        self.description_html=self.description
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug}) # name이 single인 path의 url에는 slug가 들어가는데, 이 때 slug화된 그룹명이 url에 포함된다.

    class Meta:
        ordering=['name']

class GroupMember(models.Model):
    group=models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __Str__(self):
        return self.user.username

    class Meta:
        unique_together=('group', 'user')
