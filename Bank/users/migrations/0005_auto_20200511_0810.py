# Generated by Django 3.0.6 on 2020-05-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200511_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transactionID',
            field=models.CharField(default='MplG9gagDHzQsJU', max_length=15, unique=True),
        ),
    ]
