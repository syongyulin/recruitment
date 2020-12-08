from django.urls import path,include
from jobs import views
app_name='jobs'
urlpatterns = [
    path('', views.joblist,name='joblist'),
    path('job/<int:job_id>/', views.jobdetail,name='jobdetail'),
    path("resume/add/",views.ResumeCreateView.as_view(),name="resume-add"),
    path('resume/<int:pk>', views.ResumeDetailView.as_view(), name="resume-detail"),
]
