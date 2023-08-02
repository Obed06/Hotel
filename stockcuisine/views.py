from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StockCuisine
from .serializers import StockCuisineSerializer




# STOCK CUISINE
@api_view(['GET'])
def get_stocks_cuisine(request):
    stocks = StockCuisine.objects.all()
    serialized_stocks = StockCuisineSerializer(stocks, many=True)
    return Response(serialized_stocks.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_stock_cuisine(request):
    serialized_data = StockCuisineSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

