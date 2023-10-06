from django.urls import path 
from . import views

# registering the app name space for URL names
app_name = 'document_app'


urlpatterns = [
    path('',views.editor,name='editor'),
    path('delete_document/<int:docid>/', views.delete_document,name='delete_document')
]