from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Winery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='winery_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            max_width = 600
            max_height = 400
            if img.width > max_width or img.height > max_height:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)
                img.save(self.image.path)

    REGION_CHOICES = [
        ('Regiunea viticolă a dealurilor Moldovei', 'Regiunea viticolă a dealurilor Moldovei'),
        ('Regiunea viticolă a podișului Transilvaniei', 'Regiunea viticolă a podișului Transilvaniei'),
        ('Regiunea viticolă a dealurilor Munteniei și Olteniei', 'Regiunea viticolă a dealurilor Munteniei și Olteniei'),
        ('Regiunea viticolă a dealurilor Banatului', 'Regiunea viticolă a dealurilor Banatului'),
        ('Regiunea viticolă a Crișanei și Maramureșului', 'Regiunea viticolă a Crișanei și Maramureșului'),
        ('Regiunea viticolă a teraselor Dunării', 'Regiunea viticolă a teraselor Dunării'),
        ('Nisipurile și alte terenuri favorabile din sudul țării', 'Nisipurile și alte terenuri favorabile din sudul țării'),
    ]
    region = models.CharField(max_length=100, choices=REGION_CHOICES, null=True, blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField()
    grape_varieties = models.CharField(max_length=200)
    administrator_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    approved = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Este un obiect nou, setăm utilizatorul curent ca proprietar
            self.owner = kwargs.pop('owner', None)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

