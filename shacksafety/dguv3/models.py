from django.db import models                                                     
from django.conf import settings

from model_utils.models import TimeStampedModel                                  
                                                                                 
class Powercord(TimeStampedModel):                                               
    sticker_id = models.IntegerField(help_text='number written on the sticker')
    def __str__(self):
        return "Powercord: {}".format(self.sticker_id) 

class PowercordMeasurement(TimeStampedModel):
    powercord = models.ForeignKey(Powercord)
    iso_resistance = models.DecimalField(help_text='Isolation Resistance in Mega-Ohm', max_digits=6, decimal_places=3)
    pe_resistance = models.DecimalField(help_text='PE Resistance in milli-Ohm', max_digits=6, decimal_places=3)
    visual_inspection = models.BooleanField(default=True, help_text='has the device passed the visual inspection?') 
    test_passed = models.BooleanField(default=True, help_text='has the device passed the test?')

class safetyclass_one_device(TimeStampedModel):
    sticker_id = models.IntegerField(help_text='number written on the sticker')
    comment = models.CharField(
            max_length=255,
            blank=True,
            null=True)
    visual_inspection = models.BooleanField(default=True)
    iso_resistance = models.DecimalField(blank=True, null=True, help_text='Isolation Resistance in Mega-Ohm', max_digits=6, decimal_places=3)
    pe_resistance = models.DecimalField(help_text='PE Resistance in milli-Ohm', max_digits=6, decimal_places=3)
    pe_current = models.DecimalField(max_digits=6, decimal_places=3)
    test_passed = models.BooleanField(default=True)
    def __str__(self):
        return "Device: {}".format(self.sticker_id) 
    
class safetyclass_two_device(TimeStampedModel):
    sticker_id = models.IntegerField(help_text='number written on the sticker')
    comment = models.CharField(
            max_length=255,
            blank=True,
            null=True)
    visual_inspection = models.BooleanField(default=True)
    iso_resistance = models.DecimalField(blank=True, null=True, help_text='Isolation Resistance in Mega-Ohm', max_digits=6, decimal_places=3)
    leakage_current = models.DecimalField(blank=True, null=True, help_text='Beruehrungsspannung', max_digits=8, decimal_places=2)
    test_passed = models.BooleanField(default=True)
    def __str__(self):
        return "Device: {}".format(self.sticker_id) 
