# Generated by Django 2.2.2 on 2019-08-03 14:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20190803_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='message',
            new_name='content',
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'content')},
        ),
    ]
