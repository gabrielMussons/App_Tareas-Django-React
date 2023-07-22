from django.urls import path, include
from tasks.views import TaskViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls


# Crea un router y registra nuestro viewset.
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),  # Agrega las rutas generadas por el Router aquí.
    path('api/v1/docs/', include_docs_urls(title='Tasks API')),  # Agrega la documentación de CoreAPI.
]
