# Generated by Django 4.1.3 on 2022-12-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0015_alter_membership_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(max_length=10),
        ),
    ]
