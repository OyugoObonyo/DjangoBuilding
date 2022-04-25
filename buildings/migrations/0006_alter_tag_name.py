# Generated by Django 4.0.4 on 2022-04-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0005_tenant_building_tenants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('commercial', 'commercial'), ('residential', 'residential'), ('industrial', 'industrial')], default='residential', max_length=20),
        ),
    ]
