# Generated by Django 2.2.10 on 2020-02-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_register', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('name_book', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
