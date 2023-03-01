from rest_framework.views import APIView
from .models import Page
from .serializers import PageSerializer
from rest_framework.response import Response



class PageView(APIView):
    def get_object(self, page):
        try:
            page = Page.objects.get(pk=page + 1)
            return (page)
        except Page.DoesNotExist:
            self.get_object(page+1)

    def get(self, request):
        try:
            page = request.query_params.get("page", 0)
            page = int(page)
        except ValueError:
            page = 0
        page_object = self.get_object(page)
        serializer = PageSerializer(
            page_object,
            context={"request": request},
        )
        return Response(serializer.data)

