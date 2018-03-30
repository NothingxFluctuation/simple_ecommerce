# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
            ],
            options={
                'verbose_name': 'category',
                'ordering': ('name',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='shop.Category', related_name='products')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
