from django.contrib import admin
from .models import Destinations,Details,Booking

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Destinations, AuthorAdmin)
admin.site.register(Details, AuthorAdmin)
admin.site.register(Booking)

