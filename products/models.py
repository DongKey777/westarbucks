from django.db import models
'''
class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'
       
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

'''

class Categories(models.Model):

    menu_id = models.ForeignKey('Menu',on_delete = models.CASCADE, blank =False)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Menu(models.Model):

    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'menu'

class Drinks(models.Model):

    category_id = models.ForeignKey('Categories',on_delete = models.CASCADE, blank = False)
    korean_name = models.CharField(max_length = 45)
    english_name = models.CharField(max_length = 45)
    description = models.TextField

    class Meta:
        db_table = 'drinks'

class AllergyDrinkRel(models.Model):

    allergy_id = models.ForeignKey('Allergy',on_delete= models.CASCADE, blank= True)
    drink_id = models.ForeignKey('Drinks',on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'allergy_drink'

class Nutritions(models.Model):

    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    drink_id = models.ForeignKey('Drinks', on_delete=models.CASCADE, null=True)
    size_id = models.ForeignKey('sizes', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'nutritions'

class Images(models.Model):

    image_url = models.CharField(max_length= 2000)
    drink_id = models.ForeignKey('Drinks', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Allergy(models.Model):

    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45,null=True)
    size_fluid_ounce = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'sizes'
