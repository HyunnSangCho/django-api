from rest_framework.views import APIView
from .models import Page
from .serializers import PageSerializer
from rest_framework.response import Response



class PageView(APIView):
    def get(self, request):
        try:
            page = request.query_params.get("page", 0)
            page = int(page)
        except ValueError:
            page = 0
        page = Page.objects.get(pk=page+1)
        serializer = PageSerializer(
            page,
            context={"request": request},
        )
        return Response(serializer.data)

