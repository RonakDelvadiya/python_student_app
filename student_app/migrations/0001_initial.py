# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'School Name')),
                ('address', models.TextField(null=True, verbose_name=b'Address', blank=True)),
                ('rating', models.IntegerField(max_length=1, verbose_name=b'Rating', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name=b'EmailID')),
                ('contact_no', models.BigIntegerField(max_length=10, null=True, verbose_name=b'Contact No.', blank=True)),
                ('website', models.CharField(max_length=50, null=True, verbose_name=b'Website', blank=True)),
                ('enabled', models.BooleanField(default=True, verbose_name=b'Is active')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Last Name')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name=b'EmailID')),
                ('residence_address', models.TextField(null=True, verbose_name=b'Residence Add.', blank=True)),
                ('standard', models.IntegerField(max_length=1, verbose_name=b'Standard', choices=[(5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('roll_no', models.PositiveIntegerField(verbose_name=b'Roll No.')),
                ('fees', models.PositiveIntegerField(verbose_name=b'Fees')),
                ('enabled', models.BooleanField(default=True, verbose_name=b'Is active')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(to='student_app.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
