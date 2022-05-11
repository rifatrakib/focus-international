from django.utils.translation import gettext_lazy as _
from django.db.models import UniqueConstraint
from django.db import models


class School(models.Model):
    school_name = models.CharField(_('name of school'), max_length=100, unique=True)
    short_name = models.CharField(_('abbreviated name'), max_length=10, unique=True)
    country = models.CharField(_('country'), max_length=50)
    
    class Meta:
        indexes = [models.Index(fields=['short_name'])]
    
    def __str__(self):
        return self.school_name


class Course(models.Model):
    class DegreeChoices(models.TextChoices):
        BACHELOR = 'b', _('bachelor degree')
        MASTERS = 'm', _('masters degree')
        PHD = 'p', _('doctorate degree')
    
    course_name = models.CharField(_('name of course'), max_length=100)
    degree_type = models.CharField(_('type of degree'), max_length=1, choices=DegreeChoices.choices)
    
    class Meta:
        indexes = [
            models.Index(fields=['course_name']),
            models.Index(fields=['degree_type']),
            models.Index(fields=['course_name', 'degree_type']),
        ]
        constraints = [
            UniqueConstraint(fields=['course_name', 'degree_type'], name='unique_degree_course'),
        ]
    
    def __str__(self):
        return f'{self.get_degree_type_display()} in {self.course_name}'
