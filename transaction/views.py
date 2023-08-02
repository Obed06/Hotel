from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer





# TRANSACTION
@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    serialized_transactions = TransactionSerializer(transactions, many=True)
    return Response(serialized_transactions.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_transaction(request):
    serialized_data = TransactionSerializer(data=request.data)
    
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)