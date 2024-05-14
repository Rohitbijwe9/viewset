from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

class Productview(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']  

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        pro = Product.objects.all()
        serializer = self.serializer_class(pro, many=True)
        return Response({'message': 'Data retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        pro = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(pro)
        return Response({'message': 'Data retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk):
        pro = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(pro, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({"message": "Data is not valid"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        pro = get_object_or_404(self.queryset, pk=pk)
        pro.delete()
        return Response({'massage':'data deleted'},status=status.HTTP_204_NO_CONTENT)
