# Generated by Django 4.0.5 on 2022-07-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
