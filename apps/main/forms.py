from django.forms import ModelForm
from .models import YourContact


class ContactsForm(ModelForm):
    class Meta:
        model = YourContact
        fields = ['address', 'email', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactsForm, self).__init__(*args, **kwargs)
        self.fields['your_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'your name please',
        })
        self.fields['your_email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'your email please',
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'write subject please',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'your message please',
            'rows': 5,
            'cols': 50,
        })