from django.urls import path
from CurdOperationSimpleApp import views

urlpatterns = [

    path('',views.home_view,name='home'),
    path('Create/',views.Create_view,name='Create'),
    path('Retrieve/',views.Retrieve_view,name='Retrieve'),
    path('Update/',views.Update_view,name='Update'),
    path('delete/',views.delete_view,name='delete')
]
