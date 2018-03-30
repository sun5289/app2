from django import forms
from .models import GuessNumber

class PostForm(forms.ModelForm):    # 폼을 입력받기위한 함수
    class Meta:
        model = GuessNumber
        fields = ('name','text',)
        
