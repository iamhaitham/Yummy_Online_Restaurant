# Generated by Django 3.2.3 on 2021-06-05 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_register_app', '0003_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
