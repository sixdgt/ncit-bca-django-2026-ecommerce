from django.shortcuts import redirect, render
from app_carts.models import Cart, Wishlist
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart_page(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    print("LOGGED IN USER:", request.user, request.user.id)
    print("ALL CART ITEMS:", [(i.user.id, i.product.title) for i in cart_items])
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'pages/cart.html', context)

@login_required
def wishlist_page(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user)
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'pages/wishlist.html', context)

@login_required
def add_to_cart(request, product_id):
    user = request.user

    cart_item = Cart.objects.filter(user=user, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(user=user, product_id=product_id, quantity=1)

    return redirect('cart.page')

@login_required
def remove_from_cart(request, product_id):
    user = request.user
    Cart.objects.filter(user=user, product_id=product_id).delete()
    return redirect('cart.page')

@login_required
def add_to_wishlist(request, product_id):
    user = request.user
    Wishlist.objects.get_or_create(user=user, product_id=product_id)
    return redirect('wishlist.page')

@login_required
def remove_from_wishlist(request, product_id):
    user = request.user
    Wishlist.objects.filter(user=user, product_id=product_id).delete()
    return redirect('wishlist.page')

@login_required
def update_cart_item(request, product_id):
    user = request.user
    cart_item = Cart.objects.get(user=user, product_id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart.page')