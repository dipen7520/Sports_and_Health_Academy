# Generated by Django 3.2.3 on 2021-06-15 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_contact_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='msg',
            new_name='message',
        ),
    ]
