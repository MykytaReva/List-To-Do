from django.contrib import admin
from django.urls import path, include
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),

    path('accounts/', include('accounts.urls')),
    path('todo/', include('todo.urls')),

    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
