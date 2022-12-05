from django.forms import ModelForm
from .models import Tweets

class TweetForm(ModelForm):
    class Meta:
        model = Tweets
        fields = '__all__'