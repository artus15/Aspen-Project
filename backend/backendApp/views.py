
from backendApp.models import PlayerClass
from backendApp.serializers import PlayerClassSerializer

from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from warGame.warGame import *

from django.views.decorators.csrf import requires_csrf_token

class PlayerClassView(viewsets.ModelViewSet):
    serializer_class = PlayerClassSerializer
    queryset = PlayerClass.objects.all()


@api_view(['POST'])
def createPlayer(request, *args, **kwargs):
    user_object = JSONParser().parse(request)
    serializer = PlayerClassSerializer(data=user_object)
    print(user_object)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getPlayers(request):
    user = PlayerClass.objects.all()
    serializer = PlayerClassSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPlayersByName(request, name):
    user = PlayerClass.objects.get(name=name)
    serializer = PlayerClassSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PATCH'])
def updatePlayerInfo(request, pk, *args, **kwargs):
    user_object = PlayerClass.objects.get(id=pk)
    data = request.data
    user_object.name = data.get("name", user_object.name)
    user_object.password = data.get("password", user_object.password)
    user_object.wins = data.get("wins", user_object.wins)
    user_object.save()
    serializer = PlayerClassSerializer(user_object)
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePlayer(request, pk):
    player = PlayerClass.objects.get(id=pk)
    PlayerClass.delete(player)
    return Response('Player {} Deleted'.format(player.name))

@requires_csrf_token
def home(request):
    players = PlayerClass.objects.all()
    context = {'players': players}
    return render(request, 'home.html', context)

@csrf_exempt
@api_view(['PATCH'])
def playWar(request):
    data = request.data
    name1 = data.get("name1")
    name2 = data.get("name2")
    name = play(name1, name2)[1]
    player = PlayerClass.objects.get(name=name)
    player.wins = data.get("wins", player.wins)+1
    player.save()
    serializer = PlayerClassSerializer(player)
    return Response("{} wins for the {}th time".format(request.data.get("name", player.name), request.data.get("wins", player.wins)))
