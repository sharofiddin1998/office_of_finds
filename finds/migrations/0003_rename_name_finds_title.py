# Generated by Django 4.1.5 on 2023-02-05 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finds', '0002_alter_category_name_alter_finds_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finds',
            old_name='name',
            new_name='title',
        ),
    ]