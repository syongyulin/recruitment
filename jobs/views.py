from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from jobs.models import Job,Cities,JobTypes,Resume
# Create your views here.

# Function-based-view
def joblist(request):
    job_list = Job.objects.order_by('job_type')
    context = {
        "job_list": job_list
    }
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]

    # return HttpResponse(template.render(context))
    return render(request,'joblist.html',context)

def jobdetail(request, job_id):
    job_single = Job.objects.get(id=job_id)
    # job_single = Job.objects.get(pk=job_id)
    job_single.city_name = Cities[job_single.job_city][1]
    context = {
        'job_single':job_single,
    }

    # return HttpResponse(template.render({'job_single': job_single}))
    return render(request,'jobdetail.html',context)


# mixin是多继承，为了减少继承的层次关系，不只是python中有mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# GCBV  Class-bases-general-view
class ResumeCreateView(LoginRequiredMixin,CreateView):
    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ['username','city','phone','email','apply_position','gender',
              'bachelor_school','master_school','major','degree',
              'candidate_introduction','work_experience','project_experience']

    # 从url请求参数代入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    # 建立关联到当前用户
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


from django.views.generic.detail import DetailView
class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume_detail.html'





