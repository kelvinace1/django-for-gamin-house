from django.urls import path
from .views import Home, DebtList, DebtCreate, DebtDetail, DebtUpdate, DebtDelete

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('debts/', DebtList.as_view(), name='debt_list'),
    path('create/', DebtCreate.as_view(), name='debt_create'),
    path('debt/<int:pk>/', DebtDetail.as_view(), name='debt_detail'),
    path('debt/<int:pk>/update', DebtUpdate.as_view(), name='debt_update'),
    path('debt/<int:pk>/delete', DebtDelete.as_view(), name='debt_delete'),
]