from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','MilkShake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CH','Cheese'),
    ('IC','Ice Cream'),
)

class Product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

    #brand = models.CharField(max_length=20)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    # slug = models.SlugField()
