import random
from rest_framework.views import APIView
from .models import Page
from .serializers import PageSerializer
from rest_framework.response import Response



class PageView(APIView):
    def get_object(self, page):
        try:
            page = Page.objects.get(pk=page+1)
            return (page)
        except Page.DoesNotExist:
            page_count = Page.objects.count()
            page_random = random.randint(0, int(page_count))
            return self.get_object(page_random)


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

