from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in yout bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HU95hHuoYUQopmPq4ifewbjMYIqC2kCYZsv0kqcYFXJTstyLRHT9hZUFz0mWvrabuaX32fDu1bqlfdmCj8x5uoM00xTT40LS5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
