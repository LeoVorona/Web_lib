# Generated by Django 4.0.6 on 2022-07-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_bin_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Размер')),
                ('cost', models.IntegerField(null=True, verbose_name='Цена')),
                ('adres', models.CharField(default='Армавирская', max_length=200, verbose_name='Адрес')),
                ('bal', models.BooleanField(default=True, verbose_name='Балкон')),
            ],
        ),
        migrations.RemoveField(
            model_name='bin',
            name='is_active',
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, null=True, verbose_name='Активен'),
        ),
    ]
