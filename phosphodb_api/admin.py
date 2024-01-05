from django.contrib import admin
from . models import Pmid,ExpCondition,CellTypeDisease,CellOrTissue,PmidCellTypeDisease


admin.site.register(Pmid)
admin.site.register(ExpCondition)
admin.site.register(CellTypeDisease)
admin.site.register(CellOrTissue)
admin.site.register(PmidCellTypeDisease)