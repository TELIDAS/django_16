from django.contrib import admin
from .models import Shows, ShowComment, ShowsUser

admin.site.register(Shows)
admin.site.register(ShowComment)
admin.site.register(ShowsUser)
