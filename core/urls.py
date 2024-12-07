# core/urls.py
from django.urls import path

from .views import HomePageView , AboutPageView, HasVoted, CreateCBView, DetailView, UpdateCBView, UpdateGCBView, HasNotVoted, DeleteCBView #  AboutView,, 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('create/', CreateCBView.as_view(), name='create'),
    path('read/', DetailView.as_view(), name='read'),
    path('<str:id>/update/', UpdateGCBView.as_view(), name='update'),
    path('delete/', DeleteCBView.as_view(), name='delete'),
    path('youvoted/', HasVoted.as_view(), name='created'),
    path('you_have_not_voted/', HasNotVoted.as_view(), name='notcreated'),
    # path('about/', AboutView.as_view(), name='about'),
]