from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Message, Ticket
from .permissions import IsOwnerOrReadOnly
from .serializers import (MessageSerializer, TicketSerializer,
                          TicketUpdateStatusSerializer)


class Home(ListView):
    model = Ticket
    template_name = 'chat/home.html'


class TicketAPIList(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Ticket.objects.all()


class TicketUpdateStatusView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateStatusSerializer
    permission_classes = (IsAdminUser,)


class TicketAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdminUser,)


class MessageUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser,)


class MessageTextView(generics.ListCreateAPIView):
    queryset = Message.objects.filter(ticket__in=Ticket.objects.all())
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'chat/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'chat/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
