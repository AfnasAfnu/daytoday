from . import views
from django.urls import path

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

    path('cbvhome/',views.TaskListview.as_view(),name='cbvany'),
    path('cbvnewdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvnewdetail'),
    path('cbvnewupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvnewupdate'),
    path('cbvnewdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvnewdelete')
#<int:id chaned to pk

    # path('details/',views.details,name='details')
]
