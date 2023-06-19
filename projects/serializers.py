from rest_framework import serializers

# aca le decimos que esto esta basado en un modelo que ya he creado previamente
# desde aca django sabra que responder cuando se haga una peticion post, get, etc
from .models import Project


#  creamos una clase
#  heredamos desde serializer ModelSerializer esto me convierte un modelo en datos que van a poder ser consultado
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

        # campos que podran ser consultados
        fields = ("id", "title", "description", "technology", "created_at")

        # campos que quieron solo lectura, para que no los modifiquen, esto debe ser una tupla sino lo lee como string
        read_only_fields = ("created_at",)
