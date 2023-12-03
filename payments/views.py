from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe


def index_payments(request):
    return render(request, "payments/index_payments.html")

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                customer_email = request.user.email,
                success_url = domain_url + 'payments/' + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url = domain_url + 'payments/' + 'cancelled/',
                payment_method_types = ['card'],
                mode = 'payment',
                line_items = [
                    {
                        # 'name': 'School Fees',
                        # 'quantity': 1,
                        # 'currency': 'ngn',
                        # 'amount': 6000000
                        'quantity': 1,
                        'price_data': {
                            'product_data': {
                                'name': 'School Fees',
                                'description': 'School Fees for first semester',
                            },
                            'unit_amount': 6000000,
                            'currency': 'ngn'
                        }
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe_api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload += request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        print('Payment was successful.')

        return HttpResponse(status=200)


def success(request):
    return render(request, "payments/success.html")


def cancelled(request):
    return render(request, "payments/cancelled.html")