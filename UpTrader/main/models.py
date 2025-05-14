from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse, NoReverseMatch

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    menu_name = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def clean(self):
        if not self.url and not self.named_url:
            raise ValidationError("Укажите URL или named_URL")
        if self.url and self.named_url:
            raise ValidationError("Укажите лишь 1 параметр либо URL, либо named_URL")
    
    @property
    def get_url(self):
        if self.url:
            return self.url
        try:
            return self.parent.get_url + self.named_url + '/'
        except :
            return '#'
    
    def __str__(self):
        return self.name
    