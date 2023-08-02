from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StockMagasin
from .serializers import StockMagasinSerializer




# STOCK MAGASIN
@api_view(['GET'])
def get_stocks_magasin(request):
    stocks = StockMagasin.objects.all()
    serialized_stocks = StockMagasinSerializer(stocks, many=True)
    return Response(serialized_stocks.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_stock_magasin(request):
    serialized_data = StockMagasinSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)