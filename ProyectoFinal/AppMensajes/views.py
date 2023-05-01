from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import *

# Create your views here.

class ConversacionListView(LoginRequiredMixin, ListView):
    model = Mensajes
    context_object_name = 'conversaciones'
    template_name = 'conversacion_list.html'

    def get_queryset(self):
        return Mensajes.objects.filter(
            models.Q(remitente=self.request.user) | models.Q(destinatario=self.request.user)
        ).distinct().order_by('-timestamp')


class ConversacionCreateView(LoginRequiredMixin, CreateView):
    model = Mensajes
    fields = ['destinatario', 'mensaje']
    template_name = 'conversacion_create.html'
    success_url = reverse_lazy('AppMensajes:Inbox')

    def form_valid(self, form):
        remitente = self.request.user
        form.instance.remitente = remitente
        return super().form_valid(form)


class ConversacionDetailView(LoginRequiredMixin, DetailView):
    model = Mensajes
    context_object_name = 'conversacion'
    template_name = 'conversacion_detail.html'

    def get_object(self, queryset=None):
        room_id = self.kwargs['room_id']
        room = get_object_or_404(Mensajes, id=room_id)
        if room.remitente != self.request.user and room.destinatario != self.request.user:
            return redirect('AppMensajes:Inbox')
        return room