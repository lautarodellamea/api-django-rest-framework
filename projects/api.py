from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


# creamos la clase y le decimos de donde hereda
class ProjectViewSet(viewsets.ModelViewSet):
    # que consultas podremos hacer
    queryset = Project.objects.all()

    # permisos quien tendra permisos, que aplicacion cliente
    # en este caso usaremos "AllowAny" cualquier aplicacion cliente podra solicitar datos a mi api
    # podesmos cambiarlo con un "isAutthenticated" para comprobar si esta autenticado
    permission_classes = [permissions.AllowAny]

    # a partir de que serializer estara usando estos datos, como lo va a convertir
    serializer_class = ProjectSerializer
