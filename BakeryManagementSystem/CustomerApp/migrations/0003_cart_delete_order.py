# Generated by Django 4.1 on 2022-08-22 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0009_alter_item_item_name'),
        ('CustomerApp', '0002_order_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AdminApp.item')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
