from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/', 
         CommentViewSet.as_view({
             'get': 'list',
             'post': 'create'
         })),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         })),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]