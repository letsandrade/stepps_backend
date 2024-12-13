from django.contrib import admin
from .models import ChartModel, DataPointModel, IndicatorModel, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms

# Modify UserProfileAdmin to include email from the related User model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'profile_picture', 'user_email')  # Add 'user_email'
    search_fields = ('user__username', 'name', 'user__email')  # Add email to search fields

    # Add a custom method to display the email field from the related User model
    def user_email(self, obj):
        return obj.user.email  # Access email from the related User model
    user_email.admin_order_field = 'user__email'  # Allow sorting by email
    user_email.short_description = 'Email'  # Column header in admin

admin.site.register(UserProfile, UserProfileAdmin)

# Custom form to make email required in the admin
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    email = forms.EmailField(required=True)  # Make email required

# Register the custom form with the admin panel
class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(ChartModel)
class ChartModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(DataPointModel)
class DataPointModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'chart', 'label', 'value')

@admin.register(IndicatorModel)
class IndicatorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
