from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Actions, Context
from .serializers import ActionsSerializer, ContextSerializer
from .producer import publish, get_amount_unanswered_messages
# pylint: disable=no-member
# pylint: disable=unused-argument

class ActionsViewSet(viewsets.ViewSet):
    def get_all(self, request):
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

    def associatecontext(self, request, pk=None):
        actions = Actions.objects.get(id=pk)
        context = Context.objects.get(id=request.data["contextid"])
        actions.context = context
        actions.save()
        serializer = ActionsSerializer(actions)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def send(self, request, pk=None):
        actions = Actions.objects.get(id=pk)
        publish(actions)
        return Response(status=status.HTTP_201_CREATED)

    def get_amount_unanswered_messages(self, request):
        return Response({"amount":get_amount_unanswered_messages()},status=status.HTTP_200_OK)

class ContextViewSet(viewsets.ViewSet):
    def get_all(self, request):
        context = Context.objects.all()
        serializer = ContextSerializer(context,many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        context = Context.objects.get(id=pk)
        context.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        context = Context.objects.get(id=pk)
        serializer = ContextSerializer(instance=context,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
