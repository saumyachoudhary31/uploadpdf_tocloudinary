from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', FileUploadView.as_view())
# ]
from django.conf.urls import url
from .views import FileView
from .views import EntryViewSet
from . import views
urlpatterns = [
    url(r'^upload/', FileView.as_view(), name='file_view'),
    #url(r'^UIupload/', views.upload_files, name='file_upload'),
    url(
        r'^todo/',
        EntryViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='todo-list',
    ),
    # url(
    #     r'^todonew/',
    #     newviewsete.as_view({'get': 'list', 'post': 'create'}),
    #     name='todo-list',
    # ),
    path("xyz",views.xyz),
    path("newone",views.newone)

]