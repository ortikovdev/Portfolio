from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'image', 'message']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'id': 'image'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'id': 'message',
            'rows': "5",
            'cols': "50",
        })
