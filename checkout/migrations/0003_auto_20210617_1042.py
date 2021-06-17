# Generated by Django 3.2.2 on 2021-06-17 10:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0002_auto_20210611_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email_address',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart_total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=datetime.datetime(2021, 6, 17, 10, 41, 46, 910189, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default=datetime.datetime(2021, 6, 17, 10, 42, 8, 83595, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default=datetime.datetime(2021, 6, 17, 10, 42, 45, 389103, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=32),
        ),
    ]
