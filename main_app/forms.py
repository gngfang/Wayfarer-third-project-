from django.forms import ModelForm
from .models import Post, Profile

class Profile_Form(ModelForm):
    class Meta:
        model=Profile
        fields=['city']


class Post_Form(ModelForm):
    class Meta:
        model=Post
        fields=['title','content','cities']

