from django.urls import path
from .views import *

app_name = 'AppMensajes'

urlpatterns = [
    path('inbox', ConversacionListView.as_view(), name='Inbox'),
    path('nuevo-msj', ConversacionCreateView.as_view(), name='CrearConversacion'),
    path('<int:room_id>', ConversacionDetailView.as_view(), name='VerConversacion'),
    path('<int:pk>/agregar-msj/', AgregarMensajeConversacionView.as_view(), name='AgregarMensaje'),
]