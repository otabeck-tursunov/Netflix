from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import *

from .models import *
from .serializers import *


class HelloAPI(APIView):
    def get(self, request):
        data = {
            "message": "Hello World!"
        }
        return Response(data)


class AktyorlarAPI(APIView):  # :8000/aktyorlar/?name=Ulug'bek
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        id = request.query_params.get('id')
        name = request.query_params.get('name')
        chet_ellik = request.query_params.get('chet_ellik')
        search = request.query_params.get('search')
        if id is not None:
            aktyorlar = aktyorlar.filter(id=id)
        if name is not None:
            aktyorlar = aktyorlar.filter(ism__icontains=name)
        if chet_ellik is not None:
            if chet_ellik == "true":
                aktyorlar = aktyorlar.exclude(davlat="O'zbekiston")
            elif chet_ellik == "false":
                aktyorlar = aktyorlar.filter(davlat="O'zbekiston")
        if search is not None:
            aktyorlar = aktyorlar.filter(
                Q(ism__icontains=search) |
                Q(t_sana__icontains=search) |
                Q(davlat__icontains=search) |
                Q(jins__icontains=search)
            )
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        aktyor = request.data
        serializer = AktyorSerializer(data=aktyor)
        if serializer.is_valid():
            data = serializer.validated_data
            Aktyor.objects.create(
                ism=data.get('ism'),
                jins=data.get('jins'),
                davlat=data.get('davlat'),
                t_sana=data.get('t_sana'),
            )
            return Response({'success': True, 'created_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})


class AktyorAPI(APIView):
    def get(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)

    def put(self, request, pk):
        aktyor = Aktyor.objects.filter(id=pk)
        serializer = AktyorSerializer(aktyor.first(), data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            aktyor.update(
                ism=data.get('ism'),
                jins=data.get('jins'),
                davlat=data.get('davlat'),
                t_sana=data.get('t_sana'),
            )
            serializer = AktyorSerializer(aktyor.first())
            return Response({'success': True, 'updated_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})

    def delete(self, request, pk):
        aktyor = get_object_or_404(Aktyor, id=pk)
        aktyor.delete()
        return Response({"success": True, "message": "Aktyor deleted"})


class KinolarAPIView(APIView):
    def get(self, request):
        kinolar = Kino.objects.all()
        serializer = KinoSerializer(kinolar, many=True)
        return Response(serializer.data)

    def post(self, request):
        kino = request.data
        serializer = KinoSerializer(data=kino)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "created_data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KinoAPIView(APIView):
    def get(self, request, pk):
        kino = get_object_or_404(Kino, id=pk)
        serializer = KinoSerializer(kino)
        return Response(serializer.data)

    def put(self, request, pk):
        kino = get_object_or_404(Kino, id=pk)
        serializer = KinoSerializer(kino, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "updated_data": serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk):
        kino = get_object_or_404(Kino, id=pk)
        kino.delete()
        return Response({"success": True, "message": "Kino deleted"})


class KinoAktyorlarAPIView(APIView):
    def get(self, request, pk):
        kino = get_object_or_404(Kino, id=pk)
        aktyorlar = Aktyor.objects.filter(
            id__in=KinoAktyor.objects.filter(kino=kino).values_list('aktyor__id', flat=True))
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)


class IzohlarModelViewSet(ModelViewSet):
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer

    # def get_queryset(self):
    #     return izohlar

    # def list(self, request, *args, **kwargs):

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def create(self, request, *args, **kwargs):
    #
    # def destroy(self, request, *args, **kwargs):


class MyCustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


class KinolarModelViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'janr', 'yil']  # /kinolar/?search=

    pagination_class = MyCustomPagination

    def get_queryset(self):
        kinolar = Kino.objects.all()
        nom = self.request.query_params.get("nom")
        if nom is not None:
            kinolar = kinolar.filter(nom__icontains=nom)
        return kinolar

    @action(detail=True, methods=['get'])
    def aktyorlar(self, request, pk):
        kino = self.get_object()
        aktyorlar = Aktyor.objects.filter(
            id__in=KinoAktyor.objects.filter(kino=kino).values_list('aktyor__id', flat=True)
        )
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)


class AktorlarAPIView(APIView):
    def get(self, request, pk):
        aktyor = get_object_or_404(Aktyor, id=pk)
        serializer = AktorSerializer(aktyor)
        return Response(serializer.data)
