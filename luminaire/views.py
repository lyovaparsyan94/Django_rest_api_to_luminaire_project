from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import LuminaireSerializer


class LuminaireViewSet(viewsets.ModelViewSet):
    queryset = Luminaire.objects.all()
    serializer_class = LuminaireSerializer

    def get_queryset(self):
        return Luminaire.objects.all()[:3]

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# class LuminaireAPIList(generics.ListCreateAPIView):
#     queryset = Luminaire.objects.all()
#     serializer_class = LuminaireSerializer
#
#
# class LuminaireAPIUpdate(generics.UpdateAPIView):
#     queryset = Luminaire.objects.all()
#     serializer_class = LuminaireSerializer
#
#
# class LuminaireAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Luminaire.objects.all()
#     serializer_class = LuminaireSerializer

