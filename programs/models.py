from django.utils.translation import gettext_lazy as _
from django.db import models


class Program(models.Model):
    class TeachingModeChoices(models.TextChoices):
        OFFLINE = 'offline', _('Offline')
        ONLINE = 'online', _('Online')
        MIXED = 'mixed', _('Mixed')
    
    name = models.CharField(_('Title of Program'), max_length=50, unique=True)
    tagline = models.CharField(_('Sub-title of Program'), max_length=100, blank=True, null=True)
    deadline = models.DateField(_('Application Deadline'), blank=True, null=True)
    introduction = models.CharField(_('Program Introduction'), max_length=250, blank=True, null=True)
    teaching_mode = models.CharField(_('Teaching Mode'), max_length=10, choices=TeachingModeChoices.choices, blank=True, null=True)
    academic_history = models.CharField(_('Academic History'), max_length=100, blank=True, null=True)
    advantages = models.CharField(_('Program Advantages'), max_length=500, blank=True, null=True)
    description = models.CharField(_('General Description'), max_length=2000, blank=True, null=True)
    scholarships = models.CharField(_('Scholarship Infomation'), max_length=250, blank=True, null=True)
    institutions = models.CharField(_('Institutes'), max_length=500, blank=True, null=True)
    extra_information = models.JSONField(_('Additional information'), null=True, blank=True)
    
    class Meta:
        indexes = [models.Index(fields=['name'])]
    
    def __str__(self):
        return self.name
