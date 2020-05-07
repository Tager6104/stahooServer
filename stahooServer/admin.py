from django.contrib import admin
import stahooServer.models as models

admin.site.register(models.User)
admin.site.register(models.Operation)
admin.site.register(models.PartialOperation)
