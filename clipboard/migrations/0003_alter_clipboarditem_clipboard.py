# Generated by Django 4.2.4 on 2024-06-11 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clipboard', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipboarditem',
            name='clipboard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='clipboard.clipboard'),
        ),
    ]
