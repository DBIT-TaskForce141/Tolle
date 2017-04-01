from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(RfidCar)

admin.site.register(UserRfid)

admin.site.register(Transaction)

admin.site.register(TollPlaza)

admin.site.register(Wallet)

admin.site.register(WalletTransaction)

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)
