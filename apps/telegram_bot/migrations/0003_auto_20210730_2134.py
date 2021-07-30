# Generated by Django 3.1.13 on 2021-07-30 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0002_auto_20210730_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='First launch of the bot'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='user_id',
            field=models.IntegerField(unique=True, verbose_name='User ID'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='@Username'),
        ),
    ]