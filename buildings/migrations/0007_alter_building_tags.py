# Generated by Django 4.0.4 on 2022-04-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0006_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='tags',
            field=models.ManyToManyField(blank=True, to='buildings.tag'),
        ),
    ]
