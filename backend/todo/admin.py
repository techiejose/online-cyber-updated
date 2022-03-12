from django.contrib import admin
from .models import Krarecords, Returns
from .models import Jobrequest,Article

class TodoAdmin(admin.ModelAdmin):
    list_display = ('names', 'profession','idno','dob','box','county','town','mobile','email','datesend','datecompleted')
class JobAdmin(admin.ModelAdmin):
    list_display = ('names','idno','message','mobile','jobtype','datecompleted','datesend')

class ReturnsAdmin(admin.ModelAdmin):
    list_display = ('id', 'names','yourpin','employerpin','email','p9form','datesend','datecompleted')

class articleAdmin(admin.ModelAdmin):
    list_display = ('title','body','photo','author','dateposted')
# Register your models here.

admin.site.register(Krarecords, TodoAdmin)
admin.site.register(Jobrequest, JobAdmin)
admin.site.register(Article, articleAdmin)
admin.site.register(Returns, ReturnsAdmin)