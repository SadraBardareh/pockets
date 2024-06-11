# Generated by Django 4.2.3 on 2024-06-10 16:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clipboard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClipboardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=1023)),
                ('clipboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clipboard.clipboard')),
            ],
        ),
    ]
