# Generated by Django 3.1.7 on 2021-03-27 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='profiles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]