# Generated by Django 4.2.4 on 2023-08-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empoyee",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("sal", models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
