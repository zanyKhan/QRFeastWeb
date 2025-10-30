import json
from rest_framework.response import Response
from rest_framework.views import APIView

class ItemListView(APIView):
    def get(self, request):
        with open('items.json', 'r') as file:
            items = json.load(file)
        return Response(items)