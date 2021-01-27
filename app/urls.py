from app.views import PostDetail
from app.views import PostList  
from django.urls import path  

app_name = 'app'  
urlpatterns = [  
    path('', PostList.as_view(), name='post-list'),  
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),  
]