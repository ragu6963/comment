from django.db import models
from django.contrib.auth.models import User  

class Post(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True) 