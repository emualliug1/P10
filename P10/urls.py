from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ProjectViewSet, IssueViewSet, ContributorViewSet, CommentViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router1 = routers.SimpleRouter()
router1.register('projects', ProjectViewSet, basename='projects')

router2 = routers.SimpleRouter()
router2.register('users', ContributorViewSet, basename='users')
router2.register('issues', IssueViewSet, basename='issues')

router3 = routers.SimpleRouter()
router3.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/v1/", include(router1.urls)),
    path("api/v1/projects/<int:project_id>/", include(router2.urls)),
    path("api/v1/projects/<int:project_id>/issues/<int:issue_id>/", include(router3.urls)),


    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("", include('dj_rest_auth.registration.urls')),

    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/redoc", SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
    path("api/schema/swagger", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger"),
]
