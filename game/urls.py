from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', "game.views.start_hack"),
    url(r'^submit_attempt$', "game.views.submit_attempt")
)
