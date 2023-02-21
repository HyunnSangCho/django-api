from rest_framework.views import APIView
from .models import Clone
from .serializers import CloneSerializer
from rest_framework.response import Response


class CloneView(APIView):
    def get(self, request):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        clone = Clone.objects.get(pk=page)
        serializer = CloneSerializer(
            clone,
            context={"request": request},
        )
        return Response(serializer.data)

