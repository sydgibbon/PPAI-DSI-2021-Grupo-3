# Generated by Django 3.2.4 on 2021-06-21 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_auto_20210621_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='exposicion',
            name='detalles_exposicion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.detalleexposicion'),
        ),
    ]