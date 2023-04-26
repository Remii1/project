from django.contrib import admin
from django.urls import path
from Myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('recipe/',views.recipe),
    path('contact/',views.contact),

]