# Generated by Django 2.0.3 on 2018-08-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='avatar',
            field=models.ImageField(null=True, upload_to='podcasts/episodes/'),
        ),
    ]
