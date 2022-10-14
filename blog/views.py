from django.shortcuts import render
from .models import Post, Category, Author
from django.db.models import Q


def homepage(request):
    categories = Category.objects.filter(language=request.LANGUAGE_CODE)
    featured = Post.objects.filter(featured=True, categories__in=categories)
    context = {
        'object_list': featured,
        'categories': categories,
    }
    return render(request, 'homepage.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)


def about(request):
    return render(request, 'about.html')


def category_post_list(request, slug):
    category = Category.objects.get(slug=slug, language=request.LANGUAGE_CODE)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
    }
    return render(request, 'category_post_list.html', context)


def all_posts(request):
    categories = Category.objects.filter(language=request.LANGUAGE_CODE)
    posts = Post.objects.filter(categories__in=categories).order_by('-timestamp')
    context = {
        "all_posts": posts,
    }
    return render(request, "all_posts.html", context)

def search(request):
    categories = Category.objects.filter(language=request.LANGUAGE_CODE)
    queryset = Post.objects.filter(categories__in=categories)
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    context = {
        'object_list': queryset,
    }
    return render(request, "search_results.html", context)
