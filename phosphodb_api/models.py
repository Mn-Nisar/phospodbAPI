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


class Enrichment(models.Model):
    method =  models.CharField(max_length=255)

    def __str__(self):
        return self.method
    
class QuantType(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class MassSpec(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Genes(models.Model):
    gene_symbol = models.CharField(max_length=255)

    def __str__(self):
        return self.gene_symbol
    
class Accession(models.Model):
    uniprot_accession = models.CharField(max_length=255)
    fasta_seq = models.TextField()    

    def __str__(self):
        return self.uniprot_accession



class Phosphosite(models.Model):
    phosphosite = models.CharField(max_length=100)

    def __str__(self):
        return self.phosphosite

class LocalizationProb(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value
    

class ClassOneSite(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class ProfileOrDiffChoice(models.TextChoices):
    profile = 'profiling', 'profiling'
    differential = 'Differential', 'Differential'


class ProfileOrDiff(models.Model):
    name = models.CharField(max_length=50,choices=ProfileOrDiffChoice.choices)

    def __str__(self):
        return self.name
    
class Expression(models.Model):
    p_value = models.CharField(max_length=255)
    ratio = models.CharField(max_length=255)
    log2_fc =  models.FloatField()

    def __str__(self):
        return self.p_value

class ExpressionStatus(models.Model):
    expression = models.CharField(max_length=255)

    def __str__(self):
        return self.expression
    
