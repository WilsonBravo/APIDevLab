# Generated by Django 4.2.11 on 2024-03-22 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0002_rename_name_user_firstname_remove_user_phonenumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='customFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateTimeField()),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'prefers not to say')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]