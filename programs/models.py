from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from entities.models import School, Course


class Offer(models.Model):
    name = models.CharField(_('name of program'), max_length=250, unique=True)
    short_description = models.CharField(_('short description of program'), max_length=1000)
    application_deadline = models.DateField(_('application deadline for program'), blank=True, null=True)
    slug = models.SlugField(_('url ending of program'), max_length=250, blank=True, unique=True, allow_unicode=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('program', kwargs={'slug': self.slug})
    
    def save(self, **kwargs):
        if self.slug is None:
            self.slug = self.name.replace(' ', '-')
        super().save(**kwargs)


class Advantages(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    advantage = models.CharField(_('advantage of the program'), max_length=250)
    
    def __str__(self):
        return self.offer


class Program(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(_('program description'))
    
    def __str__(self):
        return f'{self.offer} - {self.course}, {self.school}'
