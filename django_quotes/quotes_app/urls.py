from django.urls import path
from . import views

app_name = 'quotes_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/<str:author>', views.author, name='author'),
    path('add_quote/', views.quote, name='add_quote'),
    path('add_tag/', views.tag, name='add_tag'),
    path('add_author/', views.add_author, name='add_author'),
    ]
