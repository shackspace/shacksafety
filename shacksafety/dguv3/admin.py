from django.contrib import admin
import reversion

from .models import (Powercord,
                     PowercordMeasurement,
                     safetyclass_one_device,
                     safetyclass_two_device,)


class PowercordMeasurementInline(admin.TabularInline):
    model = PowercordMeasurement
    extra = 1
    fields = ('pe_resistance', 'iso_resistance', 'test_passed', 'visual_inspection',)

@admin.register(Powercord)
class PowercordAdmin(reversion.VersionAdmin):
    list_display = ('sticker_id',)
    list_display_links = list_display
    search_fields = ('sticker_id',)
    inlines = [
                PowercordMeasurementInline,
              ]

@admin.register(safetyclass_one_device)
class safetyclass_one_device_Admin(reversion.VersionAdmin):
    list_display = ('sticker_id',)

@admin.register(safetyclass_two_device)
class safetyclass_two_device_Admin(reversion.VersionAdmin):
    list_display = ('sticker_id',)
