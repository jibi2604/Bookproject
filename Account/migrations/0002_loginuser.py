# Generated by Django 4.2.11 on 2024-04-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
