# Generated by Django 4.2.3 on 2023-07-24 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_bike_frame_bike_frame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikeframe',
            name='color',
        ),
        migrations.AddField(
            model_name='bike',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.color'),
        ),
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]