# Generated by Django 2.1.7 on 2019-02-24 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survaider', '0003_auto_20190224_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='adults',
            name='education',
            field=models.CharField(db_index=True, default=None, max_length=200),
        ),
    ]
