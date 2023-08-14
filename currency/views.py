from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ExchangeRate, Currency
from .serializers import ExchangeRateSerializer, CurrencySerializer




@api_view(['GET', 'POST'])
def currency_list(request):
    if request.method == 'GET':
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_exchange_rate(request):
    if request.method == "GET":
        take = ExchangeRate.objects.all()
        exchange_rate = []
        
        for all in take:
            exchange_rate.append({
                'from_currency': all.from_currency.code,
                'to_currency': all.to_currency.code,
                'exchange_rate': all.rate,
                })
        
        return Response(exchange_rate, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_exchange_rate(request):
    serializer = ExchangeRateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




