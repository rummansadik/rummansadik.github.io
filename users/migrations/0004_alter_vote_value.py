# Generated by Django 3.2.5 on 2021-07-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210725_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.CharField(choices=[('Vote', 'Vote'), ('Downvote', 'Downvote')], default='Vote', max_length=10),
        ),
    ]