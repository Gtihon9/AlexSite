from django import forms
from .models import Comment, Report_Message


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'author_name', 'email')


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report_Message
        fields = ('text', 'author_name', 'email')

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['style'] = 'resize:none; font-size: 16px; font-weight: 500;'
        self.fields['author_name'].widget.attrs['style'] = 'font-size: 16px; font-weight: 500;'
        self.fields['email'].widget.attrs['style'] = 'font-size: 16px; font-weight: 500;'


