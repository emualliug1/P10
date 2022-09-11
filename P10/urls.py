import dj_rest_auth.views
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from api.views import ProjectViewSet, IssueViewSet, ContributorViewSet, CommentViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')

project_router = routers.NestedSimpleRouter(parent_router=router, parent_prefix='projects', lookup='project')
project_router.register('users', ContributorViewSet, basename='users')
project_router.register('issues', IssueViewSet, basename='issues')

issue_router = routers.NestedSimpleRouter(parent_router=project_router, parent_prefix='issues', lookup='issue')
issue_router.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(project_router.urls)),
    path("api/", include(issue_router.urls)),
    path("api/login/", dj_rest_auth.views.LoginView.as_view(), name='Login'),
    path("api/signup/", include('dj_rest_auth.registration.urls')),
    path("api/api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger"),
]
