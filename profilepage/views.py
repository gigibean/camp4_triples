from django.shortcuts import render


# Create your views here.
def profile(request):
    return render(request, 'profile.html', {'range': range(10), })


def mr(request):
    return render(request, 'mr.html')


def songs(request):
    return render(request, 'songs.html')


def likes(request):
    return render(request, 'likes.html')


def followings(request):
    return render(request, 'followings.html')


def followers(request):
    return render(request, 'followers.html')


def comments(request):
    return  render(request, 'comments.html')
