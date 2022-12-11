# Generated by Django 4.1.3 on 2022-11-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_user_register_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_register',
            name='contact',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_register',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]