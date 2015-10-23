"""
Definition of urls for FileUpload.
"""

from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^files/?$', 'app.views.files', name='files'),
    url(r'^delete/(?P<i>\d+)/?$', 'app.views.deleteFile', name='deleteFile'),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^add$', 'app.views.add', name='add'),

    url(r'^contact$', 'app.views.contact', name='contact'),

)
