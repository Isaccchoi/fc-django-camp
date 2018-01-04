from django.shortcuts import render

from photo.models import Photo


def post_list(request):
    posts = Photo.objects.all()
    return render(request, 'photo/list.html', {"posts": posts})
