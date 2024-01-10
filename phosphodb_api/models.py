from django.db import models

class Pmid(models.Model):
    
    pmid = models.BigIntegerField(primary_key=True)

    Cell_type_disease = models.ManyToManyField("CellTypeDisease", 
                        through="PmidCellTypeDisease", 
                        related_name="pmid_cell_type_disease")

    cell_or_tissue = models.ManyToManyField("CellOrTissue", 
                        through="PmidCellOrTissue", 
                        related_name="pmid_cell_or_tissue")

    cell_or_tissue = models.ManyToManyField("CellOrTissue", 
                        through="PmidCellOrTissue", 
                        related_name="pmid_cell_or_tissue")

    profile_or_diff = models.ManyToManyField("ProfileOrDiff",
                        through="PmidProfileOrDiff",
                       related_name="pmid_cell_profile_or_diff")

    def __str__(self):
        return str(self.pmid)



class CellTypeDisease(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name
    

class ExpCondition(models.Model):
    utf8_name = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)

    pmid = models.ForeignKey(Pmid, on_delete=models.PROTECT)
    mass_spec = models.ForeignKey("MassSpec", on_delete=models.PROTECT)

    class_one_site = models.ManyToManyField("ClassOneSite", 
                        through="ExpConditionClassOneSite", 
                        related_name="exp_condtion_class_one_site")

    enrichment = models.ManyToManyField("Enrichment",   
                        through="ExpConditionEnrichment", 
                        related_name="exp_condtion_enrichment")

    quant_type = models.ManyToManyField("QuantType", 
                        through="ExpConditionQuantType", 
                        related_name="exp_condtion_quant_type")

    accession = models.ManyToManyField("Accession", 
                        through="ExpConditionAccession", 
                        related_name="exp_condtion_accession")

    def __str__(self):
        return self.name


class CellOrTissueChoice(models.TextChoices):
    C = 'C', 'C'
    T = 'T', 'T'

class CellOrTissue(models.Model):
    c_type = models.CharField(
        max_length=25,
        choices=CellOrTissueChoice.choices,
        primary_key=True
    )

    def __str__(self):
        return self.c_type


class Enrichment(models.Model):
    method =  models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.method
    
class QuantType(models.Model):
    name = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.name
    
class MassSpec(models.Model):
    name = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.name


class Genes(models.Model):
    gene_symbol = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.gene_symbol

class Species(models.Model):
    name = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.name


class Accession(models.Model):
    uniprot_accession = models.CharField(max_length=255,primary_key=True)
    fasta_seq = models.TextField()    
    is_isofrom=  models.BooleanField(default=False)
    refseq_accession = models.CharField(max_length=255,null=True)
    gene_symbol = models.ForeignKey(Genes,on_delete=models.PROTECT)
    species = models.ForeignKey(Species,on_delete=models.PROTECT)

    exp_condition = models.ManyToManyField("ExpCondition", 
                        through="ExpConditionAccession", 
                        related_name="accession_exp_condition")
    
    phosphosite = models.ManyToManyField("Phosphosite", 
                        through="AcceesionPhosphosites", 
                        related_name="accession_phosphosite")
 
    def __str__(self):
        return self.uniprot_accession



class Phosphosite(models.Model):

    site = models.CharField(max_length=100,primary_key=True)

    accession = models.ManyToManyField("Accession", 
                        through="AcceesionPhosphosites", 
                        related_name="phosphosite_accession")
    
    localization_prob = models.ManyToManyField("LocalizationProb", 
                        through="PhosphositeLocalizationProb", 
                        related_name="phosphosite_localization_prob")
    
    
    peptide_sequence = models.ManyToManyField("PeptideSequence", 
                        through="PhosphositePeptideSequence", 
                        related_name="phosphosite_peptide_sequence")
    
    modif_sequence = models.ManyToManyField("ModifSequence", 
                        through="PhosphositeModifSequence", 
                        related_name="phosphosite_modif_sequence")

    expression_val = models.ManyToManyField("ExpressionVal", 
                        through="PhosphositeExpressionVal", 
                        related_name="phosphosite_expression_val")

    def __str__(self):
        return self.site

class LocalizationProb(models.Model):
    value = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.value
    

class ClassOneSite(models.Model):
    name = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.name


class ProfileOrDiffChoice(models.TextChoices):
    profile = 'profiling', 'profiling'
    differential = 'Differential', 'Differential'


class ProfileOrDiff(models.Model):
    name = models.CharField(max_length=50,choices=ProfileOrDiffChoice.choices,primary_key=True)

    def __str__(self):
        return self.name
    
class ExpressionVal(models.Model):
    p_value = models.CharField(max_length=255)
    ratio = models.CharField(max_length=255)
    log2_fc =  models.FloatField()

    expression_status = models.ManyToManyField("ExpressionStatus", 
                        through="ExpressionValExpressionStatus", 
                        related_name="expression_val_expression_status")

    def __str__(self):
        return self.p_value

class ExpressionStatus(models.Model):
    expression = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.expression
    
class PeptideSequence(models.Model):
    seq = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.seq


class ModifSequence(models.Model):
    seq = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.seq

# ==========================All the linking table==============================
    

# ============CellTypeDisease and Pmid==============

class PmidCellTypeDisease(models.Model):
    pmid = models.ForeignKey(
       Pmid , on_delete=models.PROTECT, related_name="pmid_cell_type_disease_PM"
    )
    cell_type_disease = models.ForeignKey(
        CellTypeDisease, on_delete=models.PROTECT, related_name="pmid_cell_type_disease_CTD"
    )

    class Meta:
        unique_together = ("pmid","cell_type_disease")


# ============CellOrTissue and Pmid==============

class PmidCellOrTissue(models.Model):
    pmid = models.ForeignKey(
       Pmid , on_delete=models.PROTECT, related_name="pmid_cell_Or_tissue_PM"
    )
    cell_or_tissue = models.ForeignKey(
        CellOrTissue, on_delete=models.PROTECT, related_name="pmid_cell_Or_tissue_CT"
    )

    class Meta:
        unique_together = ("pmid","cell_or_tissue")



# =============Pmid and ProfileOrDiff=======

class PmidProfileOrDiff(models.Model):

    pmid = models.ForeignKey(
       Pmid , on_delete=models.PROTECT, related_name="pmid_profile_diff_PM"
    )
    profile_or_diff = models.ForeignKey(
        ProfileOrDiff, on_delete=models.PROTECT, related_name="pmid_profile_diff_POD"
    )

    class Meta:
        unique_together = ("pmid","profile_or_diff")


# ============ExpCondition AND ClassOneSite=========

class ExpConditionClassOneSite(models.Model):
    exp_condition = models.ForeignKey(
       ExpCondition , on_delete=models.PROTECT, related_name="exp_condition_class_one_site_EXP"
    )
    class_One_site = models.ForeignKey(
        ClassOneSite, on_delete=models.PROTECT, related_name="exp_condition_class_one_site_COS"
    )

    class Meta:
        unique_together = ("exp_condition","class_One_site")


# ============ExpCondition AND Enrichment============

class ExpConditionEnrichment(models.Model):
    exp_condition = models.ForeignKey(
       ExpCondition , on_delete=models.PROTECT, related_name="exp_condition_enrichment_EXP"
    )
    enrichment = models.ForeignKey(
        Enrichment, on_delete=models.PROTECT, related_name="exp_condition_enrichment_EN"
    )

    class Meta:
        unique_together = ("exp_condition","enrichment")

# ============ExpCondition AND QuantType============


class ExpConditionQuantType(models.Model):
    exp_condition = models.ForeignKey(
       ExpCondition , on_delete=models.PROTECT, related_name="exp_condition_quant_type_EXP"
    )
    quant_type = models.ForeignKey(
        QuantType, on_delete=models.PROTECT, related_name="exp_condition_quant_type_QT"
    )

    class Meta:
        unique_together = ("exp_condition","quant_type")



# ============ExpCondition AND Accession============

class ExpConditionAccession(models.Model):
    exp_condition = models.ForeignKey(
       ExpCondition , on_delete=models.PROTECT, related_name="exp_condition_accession_EXP"
    )
    accession = models.ForeignKey(
        Accession, on_delete=models.PROTECT, related_name="exp_condition_accession_ACC"
    )

    class Meta:
        unique_together = ("exp_condition","accession")

# =====================Accession and Phosphosite=======
        
class AcceesionPhosphosites(models.Model):
    accession = models.ForeignKey(
       Accession , on_delete=models.PROTECT, related_name="accession_phosphosite_ACC"
    )
    phosphosite = models.ForeignKey(
        Phosphosite, on_delete=models.PROTECT, related_name="accession_phosphosite_PH"
    )

    class Meta:
        unique_together = ("accession","phosphosite")


# =============Phosphosite and PeptideSequence=======

class PhosphositePeptideSequence(models.Model):

    phosphosite = models.ForeignKey(
       Phosphosite , on_delete=models.PROTECT, related_name="phosphosite_peptideSequence_PH"
    )
    peptide_sequence = models.ForeignKey(
        PeptideSequence, on_delete=models.PROTECT, related_name="phosphosite_peptideSequence_PS"
    )

    class Meta:
        unique_together = ("phosphosite","peptide_sequence")



# =============Phosphosite and ModifSequence=======

class PhosphositeModifSequence(models.Model):

    phosphosite = models.ForeignKey(
       Phosphosite , on_delete=models.PROTECT, related_name="phosphosite_modif_sequence_PH"
    )
    modif_sequence = models.ForeignKey(
        ModifSequence, on_delete=models.PROTECT, related_name="phosphosite_modif_sequence_MS"
    )

    class Meta:
        unique_together = ("phosphosite","modif_sequence")


# =============Phosphosite and LocalizationProb=======

class PhosphositeLocalizationProb(models.Model):

    phosphosite = models.ForeignKey(
       Phosphosite , on_delete=models.PROTECT, related_name="phosphosite_localization_prob_PH"
    )
    localization_prob = models.ForeignKey(
        LocalizationProb, on_delete=models.PROTECT, related_name="phosphosite_localization_prob_LP"
    )

    class Meta:
        unique_together = ("phosphosite","localization_prob")


# =============Phosphosite and ExpressionVal=======

class PhosphositeExpressionVal(models.Model):

    phosphosite = models.ForeignKey(
       Phosphosite , on_delete=models.PROTECT, related_name="phosphosite_ExpressionVal_PH"
    )
    expression_val = models.ForeignKey(
        ExpressionVal, on_delete=models.PROTECT, related_name="phosphosite_ExpressionVal_EV"
    )

    class Meta:
        unique_together = ("phosphosite","expression_val")


# =============ExpressionVal and ExpressionStatus=======


class ExpressionValExpressionStatus(models.Model):

    expression_val = models.ForeignKey(
       ExpressionVal , on_delete=models.PROTECT, related_name="expression_val_expression_status_EV"
    )
    expression_status = models.ForeignKey(
        ExpressionStatus, on_delete=models.PROTECT, related_name="expression_val_expression_status_ES"
    )

    class Meta:
        unique_together = ("expression_val","expression_status")