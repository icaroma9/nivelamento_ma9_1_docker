# Generated by Django 3.1 on 2020-08-05 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_auto_20200805_1016"),
    ]

    operations = [
        migrations.RenameField(
            model_name="produto", old_name="name", new_name="nome",
        ),
    ]
