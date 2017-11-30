from django.conf.urls import url
from . views import add_tutor, welcome


urlpatterns = [
    url(r'add_tutor', add_tutor),
    url(r'', welcome),
]
