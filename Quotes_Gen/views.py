from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quote
from django.http import HttpResponse, response
from .serializers import QuoteSerializer
from random import randint


@api_view(['GET'])

def quotesviewset(request):
    num = randint(1,40)
    prev = request.COOKIES.get("prev")
    if prev == num:
        num = randint(1,40)
    data = [Quote.objects.get(id=num)]
    serializer = QuoteSerializer(data, many=True)
    response = Response(serializer.data)
    response.set_cookie('prev', str(num))
    return response

