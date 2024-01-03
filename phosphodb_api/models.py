from django.db import models

class Pmid(models.Model):
    pmid = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.pmid


class ExpCondition(models.Model):
    name = models.CharField(max_length=1000)
    utf8_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class CellTypeDisease(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    


class CellOrTissueChoice(models.TextChoices):
    cell = 'cell', 'C'
    tissue = 'tissue', 'T'


class CellOrTissue(models.Model):
    c_type = models.CharField(
        max_length=25,
        choices=CellOrTissueChoice.choices,
    )

    def __str__(self):
        return self.name
