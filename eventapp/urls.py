
from django.contrib import admin
from django.urls import path
from eventapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("corona_data/", views.corona),

]
