from django.urls import path
from . import views


urlpatterns = [

    # ========================= HOME =========================

    path('',views.index,name='index'),

    # ========================= HOME =========================


]