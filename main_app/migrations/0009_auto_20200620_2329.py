# Generated by Django 3.0.7 on 2020-06-20 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_post_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cities',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='main_app.City'),
        ),
    ]
