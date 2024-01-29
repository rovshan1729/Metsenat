from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Dashboard)
admin.site.register(models.Sponsors)
admin.site.register(models.SponsorsFilter)
admin.site.register(models.AboutSponsor)
admin.site.register(models.EditingIndividual)
admin.site.register(models.EditingLegalEntity)
admin.site.register(models.Students)
admin.site.register(models.StudentFilter)
admin.site.register(models.AddStudent)
admin.site.register(models.AboutStudent)
admin.site.register(models.EditStudent)
admin.site.register(models.EditSponsor)
admin.site.register(models.AddSponsor)
