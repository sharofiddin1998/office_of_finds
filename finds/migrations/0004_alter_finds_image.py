# Generated by Django 4.1.5 on 2023-02-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finds', '0003_rename_name_finds_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finds',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
