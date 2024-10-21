from django.urls import path
from myapp import views
# home, login_view, register, dashboard, add_bill,  delete_bill, logout_view,edit_bill

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('query/', views.query, name='query'),
    path('querydata/<str:x>', views.querydata, name='querydata'),
    path('edit/<int:x>', views.edit, name='edit'),
    path('update/<int:x>/', views.update, name='update'),
    # path('edit_bill/<int:x>/', edit_bill, name='edit_bill'),
    # path('delete_bill/<int:bill_id>/', delete_bill, name='delete_bill'),
    path('logout/', views.logout, name='logout'),
     path('delete/<int:x>/<str:y>', views.delete, name='delete'),
    
    # path('query/',query,name='query')
]
