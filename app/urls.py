from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPwdChangeForm

urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),    
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
    
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),    

    path('registration/', views.CustomerRegisterationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name="login"),
    path('logout/', auth_view.LogoutView.as_view(next_page="login"), name="logout"),    
    
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPwdChangeForm, success_url='/pwdchangedone/'), name='passwordchange'),
    path('pwdchangedone/', auth_view.PasswordChangeView.as_view(template_name='app/pwdchangedone.html'), name="pwdchangedone"),
    path('pwd-reset/', auth_view.PasswordResetView.as_view(), name='pwd-reset'),
    path('checkout/', views.checkout, name='checkout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
