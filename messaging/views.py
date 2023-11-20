from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Message
from .forms import MessageForm
from accounts.models import User


@login_required(login_url="login")
def index_messages(request):

    user_messages = Message.objects.filter(recipient=request.user)
    user_messages_total = user_messages.count()

    context = {
        "user_messages": user_messages,
        "total": user_messages_total
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


def send_message_to_multiple_users(request):

    if request.method == "POST":
        pass

    pass
