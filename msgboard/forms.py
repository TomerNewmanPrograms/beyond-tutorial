from django import forms
from .models import Message


# messege class
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('author', 'text')
