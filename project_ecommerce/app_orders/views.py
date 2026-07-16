from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app_orders.models import Order, OrderItem
from app_carts.models import Cart
from django.shortcuts import get_object_or_404
from django.db import transaction

# Create your views here.
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'users/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'users/order_detail.html', {'order': order})

@login_required
def checkout_page(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    if not cart_items.exists():
        return redirect('cart_view')

    total_price = sum(item.total_price for item in cart_items)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        with transaction.atomic():
            # Create Order
            order = Order.objects.create(
                user=user,
                total_price=total_price,
                name=name,
                address=address,
                payment_method=payment_method
            )

            # Create Order Items
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # Clear Cart
            cart_items.delete()

        return redirect('order_detail', order_id=order.id)

    return render(request, 'pages/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })