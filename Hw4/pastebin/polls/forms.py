from django import forms
from polls.models import Paste 

class pasteForm(forms.ModelForm):
    title=forms.CharField(max_length=200)
    text=forms.TextInput()
    date=forms.DateTimeField()
    class Meta:
        model = Paste
        fields = ('title', 'text', 'date')