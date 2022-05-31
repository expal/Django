from authapp.apps import AuthappConfig
from django.urls import path
from authapp.views import CustomLoginView, CustomRegisterView, CustomLogoutView, CustomEditView

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name ='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit/', CustomEditView.as_view(), name='edit')

]
