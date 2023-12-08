from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .payment_types import *

import stripe


@login_required(login_url="login")
def index_payments(request):
    return render(request, "payments/index_payments.html")


@csrf_exempt
@login_required(login_url="login")
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {"publicKey": settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
@login_required(login_url="login")
def create_checkout_session(request):
    if request.method == "GET":
        domain_url = "http://localhost:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            line_items_input = []
            line_items_input.append(
                payment_items["school_fees"][request.user.student.level]
            )
            checkout_session = stripe.checkout.Session.create(
                customer_email=request.user.email,
                success_url=domain_url
                + "payments/"
                + "success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=domain_url + "payments/" + "cancelled/",
                payment_method_types=["card"],
                mode="payment",
                line_items=line_items_input,
            )
            return JsonResponse({"sessionId": checkout_session["id"]})
        except Exception as e:
            return JsonResponse({"error": str(e)})


@csrf_exempt
@login_required(login_url="login")
def stripe_webhook(request):
    stripe_api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload += request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")

        return HttpResponse(status=200)


@login_required(login_url="login")
def success(request):
    # TODO: Store Payment Details in the database
    return render(request, "payments/success.html")


@login_required(login_url="login")
def cancelled(request):
    return render(request, "payments/cancelled.html")
