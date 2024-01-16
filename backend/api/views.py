from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class MessageAPIView(APIView):
    http_method_names = ('post',)

    def post(self, request: Request):
        return Response({'message': 'Hello World'}, 200)
