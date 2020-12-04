from django.contrib import admin
from studentsapp.models import student
from studentsapp.models import student2
class studentAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
	list_filter=('cName','cSex')
	search_fields=('cName',)
	ordering=('id',)
	
admin.site.register(student,studentAdmin)

class student2Admin(admin.ModelAdmin):
	list_display=('id','no','companyid','num','jobname','name','company','cash')
admin.site.register(student2,student2Admin)
