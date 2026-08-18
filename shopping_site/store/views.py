from django.shortcuts import render
def product1(request):
    cart = request.session.get('cart', [])
    cart.append({'name': 'Pen', 'price': 10})
    request.session['cart'] = cart
    return render(request, 'product1.html')
def product2(request):
    cart = request.session.get('cart', [])
    cart.append({'name': 'Notebook', 'price': 50})
    request.session['cart'] = cart
    return render(request, 'product2.html')
def product3(request):
    cart = request.session.get('cart', [])
    cart.append({'name': 'Bag', 'price': 500})
    request.session['cart'] = cart
    return render(request, 'product3.html')
def cart_view(request):
    cart = request.session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render(request, 'cart.html', {
        'cart': cart,
        'total': total
    })

# Create your views here.
