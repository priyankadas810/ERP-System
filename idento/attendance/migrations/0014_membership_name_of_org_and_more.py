# Generated by Django 4.1.3 on 2022-12-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0013_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='name_of_org',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membership',
            name='discount_percentage',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='membership',
            name='discounted_price',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='membership',
            name='original_price',
            field=models.IntegerField(max_length=4),
        ),
    ]