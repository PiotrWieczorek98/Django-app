# Generated by Django 4.1 on 2022-09-01 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ***REMOVED***

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=5)),
                ('configurationType', models.BooleanField(choices=[(False, 'Regular'), (True, 'Custom')***REMOVED***, default=False)),
                ('configuration', models.CharField(max_length=50)),
                ('ean', models.CharField(max_length=13)),
            ***REMOVED***,
        ),
        migrations.CreateModel(
            name='OrderEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.product')),
            ***REMOVED***,
        ),
    ***REMOVED***
