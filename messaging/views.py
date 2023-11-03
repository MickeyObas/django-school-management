from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Message
from .forms import MessageForm
from accounts.models import User


def index_messages(request):

    user_messages = Message.objects.filter(recipient=request.user)

    context = {"messages": user_messages}

    return render(request, "pages/index_messages.html", context)


def view_message(request, pk):

    message = get_object_or_404(Message, id=pk)

    context = {"message": message}

    return render(request, "pages/view_message.html", context)


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

    return render(request, "pages/send_message.html", context)


def send_message_to_multiple_users(request):

    if request.method == 'POST':
        pass

    pass