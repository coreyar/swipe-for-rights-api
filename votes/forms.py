from django import forms
from .models import Vote


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('bill_id', 'supports',)

    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
