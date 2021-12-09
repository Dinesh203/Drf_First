from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from first_app.models import Post
from first_app.serializers import PostSerializer

# Create your views here.


@csrf_exempt
def post_list(request):
    """ Post data list"""
    if request.method == 'GET':
        posts = Post.objects.all()
        print(posts)
        serializers = PostSerializer(posts, many=True)
        print(serializers.data)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = PostSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)


@csrf_exempt
def post_detail(request, pk):
    """ return post details. """
    try:
        posts = Post.objects.get(pk=pk)
        print(posts)
    except posts.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(posts)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = PostSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data)
        return JsonResponse(serializers.errors, status=400)

    elif request.method == "DELETE":
        Post.delete()
        return HttpResponse(status=204)
