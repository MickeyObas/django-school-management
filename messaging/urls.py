from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_messages, name="index_messages"),
    path("message/<int:pk>", views.view_message, name="view_message"),
    path("send_message", views.send_message, name="send_message"),
    path("delete_message", views.delete_message, name="delete_message"),
    path("add_to_favourites", views.add_to_favourites, name="add_to_favourites"),
    path(
        "remove_from_favourites",
        views.remove_from_favourites,
        name="remove_from_favourites",
    ),
]
