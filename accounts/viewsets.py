from rest_framework import status
from rest_framework.decorators import list_route

from helpers.utils import deserialize
from helpers.viewsets import BaseViewSet

from .serializers import AccountSerializer
from .models import Account
from .forms import AccountSignUpForm, AccountUpdateForm


class AccountViewSet(BaseViewSet):
    """
        Endpoints:\n
            POST        -   /accounts/login/
            POST        -   /accounts/signup/
            GET, POST    -   /accounts/me/
    """

    serializer_class = AccountSerializer
    queryset = Account.objects.filter(is_active=True)

    def authed_user(self, request):
        token_data = request.META.get('HTTP_AUTHORIZATION')
        token_key = None
        if token_data:
            token_key = token_data.replace('Token ', '')
        return Account.objects.filter(auth_token__key=token_key).first()

    @deserialize
    @list_route(methods=['post'])
    def login(self, request, data={}):
        username = data.get('username', '').strip().lower()
        password = data.get('password', '').strip()
        account = Account.objects.filter(username=username).first()
        if account:
            if account.check_password(password):
                return self.respond(obj=account)
        return self.respond(error="Username or password were incorrect", status=status.HTTP_401_UNAUTHORIZED)

    @deserialize
    @list_route(methods=['post'])
    def signup(self, request, data={}):
        account = None
        form = AccountSignUpForm(data)

        if form.is_valid():
            form.save()
            account = form.instance
            account.save()

            return self.respond(obj=account)

        return self.error_response_from_form(form)

    @deserialize
    @list_route(methods=['get', 'post'])
    def me(self, request, data={}, *args, **kwargs):
        account = self.authed_user(request)
        if account:
            if request.method == 'GET':
                return self.respond(obj=account)
            elif request.method == 'POST':
                form = AccountUpdateForm(data, instance=account)
                if form.is_valid():
                    form.save()
                    return self.respond(obj=form.instance)
                return self.error_response_from_form(form)
        return self.respond(error="Unauthorized user", status=status.HTTP_401_UNAUTHORIZED)
