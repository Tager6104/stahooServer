from django.contrib import admin
import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Operation)
admin.site.register(models.PartialOperation)
