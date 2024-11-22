from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# unregister Groups.
admin.site.unregister(Group)


# mix Profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extent User model
class UserAdmin(admin.ModelAdmin):
    model = User
    # just display username fields on the admin page
    fields = ["username"]
    inlines = [ProfileInline]


# unregister initial User
admin.site.unregister(User)

# Register your models and Profile here.
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
