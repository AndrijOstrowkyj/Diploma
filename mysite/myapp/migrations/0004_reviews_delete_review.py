# Generated by Django 4.2 on 2024-02-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews_txt', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
