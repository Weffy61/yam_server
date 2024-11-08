from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from .models import Client
from .serializers import ClientSerializer


@api_view(['POST'])
def authenticate_client(request):
    print(timezone.now())
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        uuid = serializer.validated_data.get("uuid")

        try:
            client = Client.objects.get(username=username, uuid=uuid)
            if client and client.subscription > timezone.now():
                return Response({"status": "ok"}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error"}, status=status.HTTP_401_UNAUTHORIZED)
        except Client.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
