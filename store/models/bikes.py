from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

#  Bikes

class BikeFrame(models.Model):
    size = models.FloatField()
    
    def __str__(self):
        return str(self.size)
    
class BikeBrand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
  
class Bike(models.Model):
    type_choices = (('gor', 'Gorniy'),
                    ('sport', 'Sportivniy'))
    brand = models.ForeignKey(BikeBrand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)  
    type = models.CharField(choices=type_choices, max_length=100)
    image = models.ImageField(null=True)
    frame = models.ManyToManyField(BikeFrame, blank=True, related_name="bike_frame")
    model = models.CharField(max_length=100)
    wheels = models.FloatField(default=20.0)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.brand.name