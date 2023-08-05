from django.db import models

# Create your models here.

class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_Guests = models.SmallIntegerField()
    BookingDate = models.DateTimeField() 

class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)


class MenuItem(models.Model):
    ID = models.AutoField(primary_key=True)
    MenuID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.Title} : {str(self.Price)}'
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'