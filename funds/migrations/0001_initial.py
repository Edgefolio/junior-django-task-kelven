# Generated by Django 4.0.4 on 2022-05-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('strategy', models.CharField(choices=[('arbitrage', 'Arbitrage'), ('global_macro', 'Global Macro'), ('long_short_equity', 'Long/Short Equity')], max_length=50)),
                ('aum', models.PositiveIntegerField(blank=True, null=True, verbose_name='AUM (USD)')),
                ('inception_date', models.DateField(blank=True, null=True, verbose_name='Inception Date')),
            ],
        ),
    ]