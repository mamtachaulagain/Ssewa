# Generated by Django 4.2.2 on 2023-06-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0007_alter_userdetail_contact_alter_userdetail_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='height',
            field=models.FloatField(default='1', verbose_name='Height in Ft.'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='weight',
            field=models.FloatField(default='1', verbose_name=' Weight in Kg'),
        ),
    ]
