from .models import *


def cart_count(request):
    if request.user.is_authenticated:
        return {'cart_items_count': Cart.objects.filter(user=request.user).count()}
    return {'cart_items_count': 0}


def countreview(request):
    if request.user.is_authenticated:
        return {'review_items_count': Reviews.objects.filter(user=request.user).count()}
    return {'review_items_count': 0}