from django.contrib import admin
from rcvcpfsetup.models import ConfigApp


@admin.register(ConfigApp)
class ConfigAppAdimn(admin.ModelAdmin):
    list_display = 'application', 'nameapp', 'description',
