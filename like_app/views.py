from django.views import generic
from main_blog.models import Article, Comment
from .models import Like
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.http import Http404,HttpResponseRedirect
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.apps import AppConfig


def add_like_to_item(request):
    model_type = request.POST.get("model_type")
    item_id = request.POST.get("item_id")

    model_type_obj = ContentType.objects.all().get(model=model_type)
    item = model_type_obj.get_object_for_this_type(pk=item_id)

    user = request.user

    # item = ContentType.objects.get_
    def add_like_self(self):
        new_like = Like
        new_like.user = self.user
        new_like.item = self.item
        new_like.save(self)


    return HttpResponseRedirect("main_blog:index")