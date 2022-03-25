from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client

class Main_User(models.Model):
    name = models.CharField(max_length=210)
    email = models.EmailField()
    gender = models.CharField(max_length=30, choices=[('Ayol','Ayol'),('Erkak','Erkak')])
    user = models.OneToOneField(User, models.SET_NULL, null=True)
    phone = models.CharField(max_length=13)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    avatar = models.FileField(upload_to='img/',blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=[("Bloklangan","Bloklangan"),("Bloklanmagan","Bloklanmagan")])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Mijoz'

    def save(self, *args, **kwargs):
        if self.phone is not None:
            account_sid = '#'
            auth_token = '#'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'Hello {self.name}! You are successfully registered in Alistyle! Go https://www.ravshanenergy.uz/',
                                        from_='#',
                                        to='#'
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)

class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)
    user = models.ForeignKey(Main_User, on_delete=models.CASCADE)
    default = models.BooleanField(blank=True)

    def __str__(self):
        return self.manzil

class Email(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Obunalar"            
