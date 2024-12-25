from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 연결된 USER 객체가 삭제될때 해당 Profile도 삭제되도록 한다.
    # related_name은 하단에 nickname = models.CharField()라 생성하면 외부에서 request.user.profile.nickname이라 호출할 수 있다.
    image = models.ImageField(upload_to='profile/', null=True) # media/profile/ 밑에 이미지 저장됨
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)