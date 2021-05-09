from django.urls import path
from . import views
app_name = 'post'
urlpatterns = [
    path('', views.post_list, name='post_list1'),
    path('<int:id>',views.post_detail, name='post_detail1'),
    path('create', views.post_create, name='post_create1'),
    path('<int:id>/edit', views.post_edit, name='post_edit1'),
    path('cbv', views.PostList.as_view(), name = 'cbv_post_list'),
    path('cbv/<int:pk>', views.PostDetail.as_view(), name='cbv_post_detail'),
    path('cbv/<int:pk>/edit', views.PostUpdate.as_view(), name='cbv_post_update'),
    path('cbv/create', views.PostCreate.as_view(), name='cbv_post_create')

]