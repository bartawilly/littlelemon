# Generated by Django 4.2.3 on 2023-08-04 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Inventory',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='Price',
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Inventory', models.SmallIntegerField()),
                ('MenuID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu')),
            ],
        ),
    ]