from unicodedata import name
from django.urls import path
from .views import general_views, auth_views

app_name="employee"

urlpatterns = [
    path('', general_views.employee_list, name="index"),
    path('addEmployee', general_views.add_employee, name='addEmployee'),
    path('addExcel', general_views.add_excel, name='addExcel'),
    path('logs', general_views.logs, name='logs'),
    path('logout', auth_views.Logout, name='logout')
]

auth_urlpatterns =[
    path('login', auth_views.login, name='login')    
]

urlpatterns += auth_urlpatterns