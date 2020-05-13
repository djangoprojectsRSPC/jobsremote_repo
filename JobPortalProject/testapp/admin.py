from django.contrib import admin
from testapp.models import HydJobs,BloreJobs,PuneJobs,ChennaiJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phno']

class BloreJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phno']

class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phno']

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phno']



admin.site.register(HydJobs,HydJobsAdmin)
admin.site.register(BloreJobs,BloreJobsAdmin)
admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)
