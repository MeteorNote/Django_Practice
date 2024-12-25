from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'), # 클래스형 view는 as_view()를 해줘야함
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # 특정 유저의 primary key
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'), # 특정 유저의 primary key
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]