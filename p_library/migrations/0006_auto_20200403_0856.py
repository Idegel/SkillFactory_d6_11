# Generated by Django 2.2.6 on 2020-04-03 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200325_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrowed_book_count',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers', verbose_name='Обложка'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='friend',
        ),
        migrations.AddField(
            model_name='book',
            name='friend',
            field=models.ManyToManyField(blank=True, related_name='friends', to='p_library.Friend'),
        ),
    ]
