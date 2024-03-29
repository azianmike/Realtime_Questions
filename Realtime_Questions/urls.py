from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'homePage.views.index', name='home'),
    url(r'^api/register', 'register.views.index', name='home'),
    url(r'^api/login', 'login.views.index', name='home'),
    url(r'^api/testObjectIdExists', 'login.views.testObjectIdExists', name='testObjectIdExists'),
    url(r'^api/submitQuestion', 'questionActions.views.submitQuestion', name='submitQuestion'),
    # url(r'^Realtime_Questions/', include('Realtime_Questions.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
