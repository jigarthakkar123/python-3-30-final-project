from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('seller-index',views.seller_index,name='seller-index'),
    path('checkout/',views.checkout,name="checkout"),
    path('contact/',views.contact,name="contact"),
    path('shop-details/',views.shop_details,name="shop-details"),
    path('shop-grid/',views.shop_grid,name="shop-grid"),
    path('shoping-cart/',views.shoping_cart,name="shoping-cart"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
    path('change-password/',views.change_password,name="change-password"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('new-password/',views.new_password,name="new-password"),
    path('verify-otp/',views.verify_otp,name="verify-otp"),
    path('seller-add-product/',views.seller_add_product,name="seller-add-product"),
    path('seller-view-product/',views.seller_view_product,name="seller-view-product"),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('product-details/<int:pk>/',views.product_details,name='product-details'),
    path('seller-product-edit/<int:pk>/',views.seller_product_edit,name='seller-product-edit'),
    path('seller-product-delete/<int:pk>/',views.seller_product_delete,name='seller-product-delete'),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name='add-to-wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove-from-wishlist/<int:pk>/',views.remove_from_wishlist,name='remove-from-wishlist'),
    path('add-to-cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.cart,name='cart'),
    path('remove-from-cart/<int:pk>/',views.remove_from_cart,name='remove-from-cart'),
    path('change-qty/',views.change_qty,name='change-qty'),
    path('ajax/validate_email/',views.validate_signup,name='validate_email'),
    path('create-checkout-session/', views.create_checkout_session, name='payment'),
    path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),
    path('myorder/',views.myorder,name='myorder'),
]