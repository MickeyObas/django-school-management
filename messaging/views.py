from django.shortcuts import render, get_object_or_404

from .models import Message

def index_messages(request):

    user_messages = Message.objects.filter(recipient=request.user)

    context = {
        'messages': user_messages
    }

    return render(request, 'pages/index_messages.html', context)


def view_message(request, pk):

    message = get_object_or_404(Message, id=pk)

    context = {
        "message": message
    }

    return render(request, "pages/view_message.html", context)
