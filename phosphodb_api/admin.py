from django.contrib import admin



from . models import (Pmid,CellTypeDisease,ExpCondition,CellOrTissue,Enrichment,QuantType,MassSpec,Genes,
                     Species,Accession,Phosphosite,LocalizationProb,ClassOneSite,ProfileOrDiff,ExpressionVal,
                     ExpressionStatus,PeptideSequence,ModifSequence)

admin.site.register(Pmid)
admin.site.register(ExpCondition)
admin.site.register(CellOrTissue)
admin.site.register(Genes)
admin.site.register(Species)
admin.site.register(Accession)
admin.site.register(Phosphosite)
admin.site.register(LocalizationProb)
admin.site.register(ProfileOrDiff)
admin.site.register(ExpressionVal)
admin.site.register(ExpressionStatus)
admin.site.register(CellTypeDisease)
admin.site.register(Enrichment)
admin.site.register(QuantType)
admin.site.register(MassSpec)
admin.site.register(ClassOneSite)
admin.site.register(PeptideSequence)
admin.site.register(ModifSequence)