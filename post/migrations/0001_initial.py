# Generated by Django 3.2 on 2021-04-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField()),
                ('published', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=50)),
                ('views_count', models.IntegerField(default=0)),
                ('Category', models.CharField(choices=[('Web Development', 'WD'), ('Desktop Development', 'DD')], max_length=50)),
            ],
        ),
    ]
