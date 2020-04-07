from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def post_list(request):
    return render(request, 'blog/post_list.html', {})