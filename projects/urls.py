# yo podria crear todas las rutas desde cero, pero no hay necesidad, rest framework me da un modulo especial que crea todas las rutas basicas o lo que se conoce como crud de estos datos
# urlpatterns = []

from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

# registramos la ruta, de donde esta basado, y el nombre que le quiero dar
router.register("api/projects", ProjectViewSet, "projects")
# aca ghenero 4 urls una para post,get,delete,put

# tengo que importar un urlpatterns, el router me generara las url
urlpatterns = router.urls
