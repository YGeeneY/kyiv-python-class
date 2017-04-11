from django.conf.urls import url

from .views import test, test2

urlpatterns = [
    url('^test$', test),
    url('^test2$', test2)
]
