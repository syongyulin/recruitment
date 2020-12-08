from django.contrib import admin
from jobs.models import Resume
# Register your models here.

from jobs.models import Job
class JobAdmin(admin.ModelAdmin):
    # 添加
    exclude = ("creator","created_date","modified_date")
    list_display = ("job_name","job_type","job_city","creator","created_date","modified_date")
    # 搜索配置
    search_fields = ["job_name"]
    # 筛选
    list_filter = ["job_city"]
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


from django.contrib import messages
from interview.models import Candidate
from datetime import datetime

def enter_interview_process(modeladmin,request,queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        # 把resume对象中的所有属性拷贝到candidate对象中
        # 取出简历实体的所有属性，更新
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + ',' + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request,messages.INFO,'候选人：%s 已经成功进入面试流程'%(candidate_names))
# enter_interview_process.short_Description = u'进入面试流程'
# enter_interview_process.short_descrition = u'进入面试流程'
enter_interview_process.short_description='进入面试流程'




class ResumeAdmin(admin.ModelAdmin):
    actions = (enter_interview_process,)
    list_display = (
    'username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major', 'created_date')

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    fieldsets = (
        (None, {'fields': (
            "applicant", ("username", "city", "phone"),
            ("email", "apply_position", "born_address", "gender",),
            ("bachelor_school", "master_school"), ("major", "degree"), ('created_date', 'modified_date'),
            "candidate_introduction", "work_experience", "project_experience",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Job,JobAdmin)
admin.site.register(Resume, ResumeAdmin)