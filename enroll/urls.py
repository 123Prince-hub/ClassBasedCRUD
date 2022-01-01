from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('delete/<int:uid>', views.delete.as_view(), name='delete'),
    path('<int:uid>', views.update.as_view(), name='update'),
    # path('<int:uid>', views.update, name='update'),
]