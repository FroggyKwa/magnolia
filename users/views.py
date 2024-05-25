from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class SignUpAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            return Response(data={"status": "OK"}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)