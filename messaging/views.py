from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Message
from .forms import MessageForm
from accounts.models import User

import json


@login_required(login_url="login")
def index_messages(request):

    user_messages = Message.objects.filter(recipient=request.user)
    sent_messages = Message.objects.filter(sender=request.user)
    starred_messages = user_messages.filter(is_favourite=True)
    important_messages = user_messages.filter(sender__account_type="L")
    user_messages_total = user_messages.count()
    starred_messages_total = starred_messages.count()
    important_messages_total = important_messages.count()
    sent_messages_total = sent_messages.count()

    context = {
    "user_messages": user_messages,
    "total": user_messages_total,
    "starred": starred_messages_total,
    "important_total": important_messages_total,
    "sent_total": sent_messages_total
    }

    return render(request, "pages/index_messages.html", context)


@login_required(login_url="login")
def view_message(request, pk):

    message = get_object_or_404(Message, id=pk)

    if message.recipient != request.user:
        # TODO Log unauthorized access attempts later. For now, redirect them and pretend nothing happened lmao.
        return redirect("/messages/")

    context = {"user_message": message}

    return render(request, "messaging/view_message.html", context)


# TODO Create a messaging interface with sent, outbox, received- and allow both lecturers and students to be able to send messages.


@login_required(login_url="login")
def send_message(request, pk):

    form = MessageForm()
    recipient = User.objects.get(id=pk)

    context = {"form": form, "recipient": recipient}

    if request.method == "POST":

        form = MessageForm(request.POST)

        context.update({"form": form})

        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.recipient = recipient
            new_message.save()
            messages.success(request, "Message sent successfully")
            return redirect(
                reverse("student-profile-view", kwargs={"pk": recipient.student.id})
            )
        else:
            messages.error(request, "Form filled incorrectly. Try again.")

    return render(request, "messaging/send_message.html", context)


def send_message(request):
    # TODO: Gracefully handle messages to users that do not exist
    if request.method == 'POST':
        data = json.loads(request.body)
        recipient = data['recipient']
        message_body = data['message']
        title = data['title']

        recipient = User.objects.get(email=recipient)

        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            body=message_body
            )
    
        sent_messages = Message.objects.filter(sender=request.user)
        updated_count = sent_messages.count()

        return JsonResponse({'updated-count': updated_count})


@login_required(login_url="login")
def add_to_favourites(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message_id = data['messageId']
        
        message_object = Message.objects.get(id=message_id)

        message_object.is_favourite = True
        message_object.save()

        user_favourite_messages = Message.objects.filter(recipient=request.user, is_favourite=True)

        updated_count = user_favourite_messages.count()

        return JsonResponse({"updated-count": updated_count})
    

@login_required(login_url="login")
def remove_from_favourites(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message_id = data['messageId']
        
        message_object = Message.objects.get(id=message_id)

        message_object.is_favourite = False
        message_object.save()

        user_favourite_messages = Message.objects.filter(recipient=request.user, is_favourite=True)

        updated_count = user_favourite_messages.count()

        return JsonResponse({"updated-count": updated_count})
    

def send_message_to_multiple_users(request):

    if request.method == "POST":
        pass

    pass
