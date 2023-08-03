from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer




@api_view(['GET'])
def get_exchange_rate(request, from_currency, to_currency):
    try:
        exchange_rate = ExchangeRate.objects.get(from_currency__code=from_currency, to_currency__code=to_currency)
    except ExchangeRate.DoesNotExist:
        return Response({'error': 'Exchange rate not found'}, status=404)

    response_data = {
        'from_currency': from_currency,
        'to_currency': to_currency,
        'exchange_rate': exchange_rate.rate,
    }

    return Response(response_data)





@api_view(['POST'])
def create_exchange_rate(request):
    serializer = ExchangeRateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

