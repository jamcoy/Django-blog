from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def post_detail(request, db_id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, pk=db_id)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "postdetail.html", {'post': post})


def post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def top_posts(request):
    """
    Get list of posts ordered by number of views
    Return top 5. Render to blogposts.html
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-views')[:5]
    return render(request, "blogposts.html", {'posts': posts})
