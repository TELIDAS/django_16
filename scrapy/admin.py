from django.contrib import admin
from . import models


class PlantsAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "link",
                    "title", ]
    list_filter = ["title", ]
    list_editable = ["title", ]
    search_fields = ["title", ]


class DoramaAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "link",
                    "title", ]
    list_filter = ["title", ]
    list_editable = ["title", ]
    search_fields = ["title", ]


admin.site.register(models.Plants, PlantsAdmin)
admin.site.register(models.Dorama, DoramaAdmin)
