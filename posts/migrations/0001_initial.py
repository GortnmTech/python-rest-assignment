# Generated by Django 4.2 on 2023-04-17 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/', verbose_name='Image')),
                ('posted_time', models.DateTimeField(auto_now_add=True, verbose_name='Post_posted_time')),
                ('caption', models.CharField(blank=True, max_length=50, verbose_name='Caption')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owner', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='Post_Likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]