
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Actions
from .serializers import ActionsSerializer

class ActionsViewSet(viewsets.ViewSet):
    def list(self, request):
        actions = Actions.objects.all()
        serializer = ActionsSerializer(actions,many=True)
        return Response(serializer.data)

    
    def create(self, request):
        serializer = ActionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        actions = Actions.objects.get(id=pk)
        serializer = ActionsSerializer(actions)
        return Response(serializer.data)

    def update(self, request, pk=None):
        actions = Actions.objects.get(id=pk)
        serializer = ActionsSerializer(instance=actions,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        actions = Actions.objects.get(id=pk)
        actions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    