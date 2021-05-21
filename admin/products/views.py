from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request ):
        products = Product.objects.all()
        serailizer = ProductSerializer(products , many=True)
        return Response(serailizer.data)


    def create(self, request): #/api/products
        serailizer = ProductSerializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        serailizer.save()
        return Response(serailizer.data ,status= status.HTTP_201_CREATED )


    def retrieve(self , request, pk=None):  #/api/products/<str:id>
        product= Product.objects.get(id=pk)
        serailizer =  ProductSerializer(product)
        return Response(serailizer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id = pk)
        serailizer = ProductSerializer(instance=product, data=request.data)
        serailizer.is_valid(raise_exception=True)
        serailizer.save()
        return Response(serailizer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)