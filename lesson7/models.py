from django.db import models

# Create your models here.

class Advertisements(models.Model):
    title = models.CharField('заголовок', max_leght=128 )
    description = models.TextField('описание' )
    price = models.DecimalField('цена', max_digits=10, decemal_places=2 )
    person_http = models.TextField('Ссылка на человека')
    auction = models.BooleanField('торг', help_text='отметьте, если торгуетесь' )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"Advertisement(prise={self.prise}, id={self.id}, title={self.title} )"

class Meta:
    db_table = "advertisement"