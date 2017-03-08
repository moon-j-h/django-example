from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # 이 form을 만들기 위해서 어떤 model이 사용되는지 알림 
    class Meta:
        model = Post
        fields = ('title', 'text',)

