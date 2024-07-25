from django.urls import path
from .views import hello_world, get_contract_short_info, get_contracts_list

urlpatterns = [
    path(route='',
         view=get_contract_short_info,
         name='contracts_info'),
    path(route='all',
         view=get_contracts_list,
         name='contracts_list'),
]
