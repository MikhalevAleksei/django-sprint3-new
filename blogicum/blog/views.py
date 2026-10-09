from django.shortcuts import get_object_or_404, render

from .constants import POSTS_ON_MAIN_PAGE
from .models import Category, Post


def published_posts():
    return Post.objects.published().select_related(
        'author', 'category', 'location',
    )


def index(request):
    post_list = published_posts()[:POSTS_ON_MAIN_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(published_posts(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True,
    )
    post_list = published_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
