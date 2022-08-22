from . import views
from django.urls import path
app_name = 'todo'
urlpatterns = [
    # path('',views.index,name='index'),
    # path('delete/<int:id>/',views.delete,name='delete'),
    # path('update/<int:id>/',views.update,name='update'),
    path('cview',views.TaskList.as_view(),name='cview'),
    path('cdetail/<int:pk>/',views.TaskDetail.as_view(),name='cdetail'),
    path('cupdate/<int:pk>/', views.TaskUpdate.as_view(), name='cupdate'),
    path('cdelete/<int:pk>/', views.TaskDelete.as_view(), name='cdelete'),

]
