from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from slider.models import Slider
from slider.api.serializers import SliderSerializer
from badaRest.permissions import IsAdminOrReadOnly 



class SliderList(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        slider = Slider.objects.all()
        serializer = SliderSerializer(slider, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SliderDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        slider = self.get_object(pk=pk)
        serializer = SliderSerializer(slider)
        return Response(serializer.data)


    def put(self, request, pk):
        slider = self.get_object(pk=pk)
        serializer = SliderSerializer(slider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
