# Generated by Django 5.0.2 on 2024-06-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeecafes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoCafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
