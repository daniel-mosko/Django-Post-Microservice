# Generated by Django 4.0.5 on 2022-07-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsapp', '0003_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]