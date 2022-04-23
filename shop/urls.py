
from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="shophome"),
    path("about",views.about,name="about"),
    path("contact",views.contacts,name="contact"),
    path("tracker",views.tracker,name="tracker"),
    path("search",views.search,name="search"),
    path("products/<int:myid>",views.productView,name="products"),
    path("checkout",views.checkout,name="checkout"),
    path("requesthandler",views.requesthandler,name="requesthandler"),
    
]