# Generated by Django 4.0.5 on 2022-07-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsapp', '0004_alter_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='userId',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
