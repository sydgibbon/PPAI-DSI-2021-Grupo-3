# Generated by Django 3.2.4 on 2021-06-21 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_usuario_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='sede',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.sede'),
        ),
    ]