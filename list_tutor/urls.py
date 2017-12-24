from django.conf.urls import url
from . views import add_tutor, search_tutors, welcome


urlpatterns = [
    url(r'add_tutor', add_tutor),
    url(r'search_tutors', search_tutors),
    url(r'', welcome),
]
