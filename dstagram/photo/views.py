from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from photo.models import Photo


@login_required
def post_list(request):
    posts = Photo.objects.all()
    return render(request, 'photo/list.html', {"posts": posts})

