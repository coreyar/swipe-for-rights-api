from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Account


class AccountSignUpForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'email', 'password', )

    def __init__(self, *args, **kwargs):
        super(AccountSignUpForm, self).__init__(*args, **kwargs)
        self.old_password = self.instance.password

    def save(self, commit=True, *args, **kwargs):
        account = super(AccountSignUpForm, self).save(commit=commit, *args, **kwargs)
        password = self.cleaned_data.get('password')
        if self.old_password != password and password:
            account.set_password(password)
        if commit:
            account.save()
        return account

    def clean_username(self):
        username = self.cleaned_data.get('username').strip().lower()
        if self.instance:
            if username:
                accounts = Account.objects.filter(username=username)
                accounts = accounts.exclude(id=self.instance.id)
                if accounts.exists():
                    raise forms.ValidationError(_("Username has already been used."))
            else:
                username = self.instance.username
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email') or ''
        if email:
            email = email.strip().lower()
        accounts = Account.objects.filter(email=email)
        if self.instance:
            accounts = accounts.exclude(id=self.instance.id)
        if accounts.exists():
            raise forms.ValidationError(_("Email address has already been used."))
        return email


class AccountUpdateForm(AccountSignUpForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        not_required = ['username', 'email', 'password']
        self.old_password = self.instance.password
        for field in not_required:
            self.fields[field].required = False

    def save(self, commit=True, *args, **kwargs):
        account = super(AccountUpdateForm, self).save(commit=commit, *args, **kwargs)
        password = self.cleaned_data.get('password')
        if self.old_password != password and password:
            account.set_password(password)
        if commit:
            account.save()
        return account
