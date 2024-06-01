from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from search import views
from users.default_view import index

router = routers.DefaultRouter()

router.register('building', views.BuildingViewSet, basename='building')
router.register('department', views.DepartmentViewSet, basename='department')
router.register('teacher', views.TeacherViewSet, basename='teacher')
router.register('search', views.SearchViewSet, basename='search')


urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('users.urls')),
    re_path(r"^.*$", index, name='index'),
]
