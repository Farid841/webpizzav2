# Generated by Django 4.2.1 on 2023-05-31 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("applipizza", "0002_alter_pizza_prix"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pizza",
            name="prix",
        ),
    ]