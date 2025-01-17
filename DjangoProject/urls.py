from django.urls import path
from . import views


urlpatterns=[
    path('',views.Home,name="home"),
    path('Register',views.Register,name="Register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('removefav/<str:fid>',views.removefav,name="removefav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('removecart/<str:cid>',views.remove_cart,name="removecart"),
    path('Collections',views.Collections,name="Collections"),
    path('collections/<str:name>',views.Collectionsview,name="collectionsviews"),
    path('collections/<str:cname>/<str:pname>',views.productdetailsviews,name="productdetailsviews"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    
]
