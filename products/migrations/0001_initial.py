# Generated by Django 4.0.1 on 2022-01-10 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
            ],
            options={
                'db_table': 'drinks',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_ml', models.CharField(max_length=45, null=True)),
                ('size_fluid_ounce', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kca', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('drink_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
                ('size_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.sizes')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.CreateModel(
            name='AllergyDrinkRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drinks')),
            ],
            options={
                'db_table': 'allergy_drink',
            },
        ),
    ]
