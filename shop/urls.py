from django.urls import path
from . import views
urlpatterns = [
path("", views.index, name="ShopHome"),
path("about/", views.about, name="aboutus"),
path("contact/", views.contac, name="contactus"),
path("tracker/", views.tracker, name="tracking"),
path("search/", views.tracker, name="search"),
path("productview/", views.prodView, name="search"),
path("checkout/", views.checkout, name="checkout"),
]