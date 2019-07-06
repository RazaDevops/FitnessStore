from django.contrib import admin
from FitnessStore.models import strengthprod
# Register your models here.

class strengthprodAdmin(admin.ModelAdmin):
    list_display = ('id','stprodtype','stprodweight','stprodprice','stprodpic')


admin.site.register(strengthprod,strengthprodAdmin)