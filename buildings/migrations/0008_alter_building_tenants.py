# Generated by Django 4.0.4 on 2022-04-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0007_alter_building_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='tenants',
            field=models.ManyToManyField(blank=True, to='buildings.tenant'),
        ),
    ]