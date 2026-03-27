from django.shortcuts import render

from . models import ShippingAddress

# Create your views here.


def checkout(request):

    # User with accounts --pre-fill the form
    if request.user.is_authenticated:
        try:
            # Authenticated users with shipping information
            shipping_address = ShippingAddress.objects.get(user=request.user)

            context = {
                'shipping': shipping_address,
            }
            print(context)

            return render(request, 'payment/checkout.html', context=context)
        
        except:
            # Authenticated users with no shipping information
            return render(request, 'payment/checkout.html')


    else:
        # Guess users
        return render(request, 'payment/checkout.html')


def payment_failed(request):

    return render(request, 'payment/payment-failed.html')


def payment_success(request):

    return render(request, 'payment/payment-success.html')