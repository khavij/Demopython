from django.urls import path
from . import views
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvlistview/',views.Tasklistview.as_view(),name='cbvlistview'),
    path('cbvdetails/<int:pk>/',views.Detailview.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.Updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Deleteview.as_view(),name='cbvdelete')

]
