from django.urls import path
from FitnessStore import views

urlpatterns = [
    #path('demo/', views.demo),
    path('index/', views.demo),
    path('persons/delP/<int:id>', views.delPerson),
    path('custRegister/', views.custRegister),
    path('persons/', views.ShowPersons),
    path('addPerson/', views.AddPerson),
    path('custlist/', views.showCust),
    path('persons/editp/<int:id>', views.editPerson),
    path('strengthproducts/', views.strengthProd)
]