# Generated by Django 4.2.5 on 2023-09-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0072_alter_reviewscore_label"),
    ]

    operations = [
        migrations.AddField(
            model_name="track",
            name="position",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
