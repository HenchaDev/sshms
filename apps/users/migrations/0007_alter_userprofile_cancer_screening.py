# Generated by Django 5.0.2 on 2024-03-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_userprofile_cancer_screening"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="cancer_screening",
            field=models.DateField(default="1970-01-01"),
        ),
    ]
