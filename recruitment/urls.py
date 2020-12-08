from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
# from django.utils.translation import gettext as _
urlpatterns = [
    path('i18n/', include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('inter/', include('interview.urls')),
    path('user/', include('user.urls')),
    path("grappelli/",include('grappelli.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]


# admin.site.site_header= _("北京网络科技招聘管理系统")