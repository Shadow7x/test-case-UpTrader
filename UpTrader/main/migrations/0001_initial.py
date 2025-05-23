# Generated by Django 5.2.1 on 2025-05-14 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('named_url', models.CharField(blank=True, max_length=100)),
                ('menu_name', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.menuitem')),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
    ]
