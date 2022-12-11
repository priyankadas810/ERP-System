# Generated by Django 4.1.3 on 2022-12-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_alter_user_notifications_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_type', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('original_price', models.IntegerField()),
                ('discount_percentage', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
            ],
        ),
    ]