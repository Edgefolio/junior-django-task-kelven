from django.db import models


class Fund(models.Model):
    # Note - field types / limits established to satisfy sample data and could require adjustment in live example (e.g. field length, acceptance of null/blank)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    # Strategy - uses pre-defined options
    STRATEGY_CHOICES = [
        ('arbitrage', 'Arbitrage'),
        ('global_macro', 'Global Macro'),
        ('long_short_equity', 'Long/Short Equity')
    ]
    strategy = models.CharField(max_length=50, choices=STRATEGY_CHOICES, null=False, blank=False)
    
    aum = models.PositiveIntegerField(verbose_name="AUM (USD)", null=True, blank=True)
    inception_date = models.DateField(verbose_name="Inception Date", null=True, blank=True)

    # Overrides default name in Admin with actual name value
    def __str__(self):
        return self.name