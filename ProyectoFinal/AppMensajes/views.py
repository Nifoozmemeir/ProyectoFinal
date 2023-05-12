from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
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

class AgregarMensajeConversacionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        conversacion_id = kwargs['pk']
        mensaje = request.POST.get('mensaje')
        conversacion = get_object_or_404(Mensajes, id=conversacion_id)
        user = request.user
        if user == conversacion.remitente:
            destinatario = conversacion.destinatario
        elif user == conversacion.destinatario:
            destinatario = conversacion.remitente
        else:
            return redirect('AppMensajes:Inbox')
        nuevo_mensaje = Mensajes(remitente=user, destinatario=destinatario, mensaje=mensaje)
        nuevo_mensaje.save()
        return redirect(reverse_lazy('AppMensajes:VerConversacion', kwargs={'room_id': conversacion_id}))