# Generated by Django 3.1.6 on 2021-02-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsboard', '0002_auto_20210130_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
