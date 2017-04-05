from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dead_workspace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django_cas.views.login'),
    url(r'^$','dead_app.views.index'),
    url(r'^apply','dead_app.views.apply'),
    url(r'^submitapply','dead_app.views.submitapply'),
    url(r'^submit','dead_app.views.submit'),
    url(r'^person','dead_app.views.person'),
    url(r'^per_detail','dead_app.views.person_detail'),
    url(r'^cancel_approve','dead_app.views.cancel_approve'),
    url(r'^remind_approve','dead_app.views.remind_approve'),
    url(r'^modify_apply','dead_app.views.modify_apply'),
    url(r'^modify_submit','dead_app.views.modify_submit'),
    url(r'^approve','dead_app.views.approve'),
    url(r'^per_search','dead_app.views.person_search'),
    url(r'^hisjob','dead_app.views.hisjob'),
    url(r'^detailjob','dead_app.views.detailjob'),
    url(r'^per_nopass','dead_app.views.person_nopass'),
    url(r'^per_pass','dead_app.views.person_pass'),
    url(r'^user_apply','dead_app.views.apply'),
    #url(r'^user_apply','dead_app.dead_process.user_control.user_apply'),
)

if settings.DEBUG is True:
    urlpatterns += patterns('',
            url(r'^js/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT+"/js" }),
            url(r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT+"/css" }),
            url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT+"/fonts" }),
            url(r'^images/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT+"/images" }),
    )
