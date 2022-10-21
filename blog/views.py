from django.shortcuts import render
from .models import Post, Category, Author
from django.db.models import Q


def homepage(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True, categories__in=categories)
    context = {
        'object_list': featured,
        'categories': categories,
    }
    return render(request, 'homepage.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    author_description = getattr(post.author, f'description_{request.LANGUAGE_CODE}', False)
    context = {
        'post': post,
        'author_description': author_description,
    }
    return render(request, 'post.html', context)


def about(request):
    return render(request, 'about.html')


def category_post_list(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
        "category": category
    }
    return render(request, 'category_post_list.html', context)


def all_posts(request):
    posts = Post.custom_manager.category_by_language
    context = {
        "all_posts": posts,
    }
    return render(request, "all_posts.html", context)

def search(request):
    queryset = Post.custom_manager.category_by_language
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
