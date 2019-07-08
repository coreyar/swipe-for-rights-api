from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Account


class UserAdminCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)
        not_required = ['password1', 'password2']
        for field in not_required:
            self.fields[field].required = False


class UserAccountAdmin(UserAdmin):

    """User Account Admin model."""

    add_form = UserAdminCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser', 'is_staff',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name',)
        }
    ),)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email',)
    ordering = ('username',)


# Register the new UserAccountAdmin
admin.site.register(Account, UserAccountAdmin)

# Leave these off the admin
admin.site.unregister(Group)
