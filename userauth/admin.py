from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.urls import path
from django.template.response import TemplateResponse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    # Use fieldsets instead of fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'school', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('first_name', 'last_name', 'email', 'school', 'role', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)  # replaced 'username' with 'email'
    change_password_form = AdminPasswordChangeForm

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<id>/password/',
                self.admin_site.admin_view(self.user_change_password),
                name='customuser_change_password',
            ),
        ]
        return custom_urls + urls

    def user_change_password(self, request, id, form_url=''):
        user = self.get_object(request, id)
        if user is None:
            return redirect('..')

        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, _('Password successfully changed.'))
                return redirect('..')
        else:
            form = self.change_password_form(user)

        context = {
            **self.admin_site.each_context(request),
            'title': _('Change password: %s') % user.email,
            'form': form,
            'is_popup': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
        }
        return TemplateResponse(request, 'admin/auth/user/change_password.html', context)


admin.site.register(CustomUser, CustomUserAdmin)
