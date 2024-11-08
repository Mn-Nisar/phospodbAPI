from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from phosphodb_api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r"pmid",views.PmidViewSet)
# router.register(r"gene",views.GenesViewSet)
router.register(r"gene",views.AccessionViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema",SpectacularAPIView.as_view(),name="schema"),
    path("api/schema/docs",SpectacularSwaggerView.as_view(url_name="schema")),
    path("",SpectacularSwaggerView.as_view(url_name="schema")),

]