from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Photo


def single_photo(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    response_text = '<p>{photo_id}번...{photo_id}번 사진을 보여드릴게여</p>'
    response_text += '<p><img src="{photo_url}" /></p>'

    return HttpResponse(response_text.format(photo_id=photo_id, photo_url=photo.image_file.url))


