from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class MessageAPIView(APIView):
    def get(self, request: Request):
        return Response({'message': 'Hello, world'}, 200)
