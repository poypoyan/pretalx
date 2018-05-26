# Generated by Django 2.0.5 on 2018-05-26 12:48

from django.db import migrations, models
import pretalx.submission.models.submission


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0021_answer_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='review_code',
            field=models.CharField(blank=True, default=pretalx.submission.models.submission.generate_invite_code, max_length=32, null=True),
        ),
    ]
