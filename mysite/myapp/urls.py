from django.urls import path
from myapp.views import index, contacts, indexItem, add_item, add_to_cart, view_cart, place_order, card_payment

app_name = 'myapp'


urlpatterns = [
     path('', index, name='index'),
     path('<int:my_id>', indexItem),
     path('contacts', contacts, name="contacts"),
     path('add_item', add_item, name="add_item"),
     path('add_to_cart', add_to_cart, name='add_to_cart'),
     path('card_payment/', card_payment, name='card_payment'),  # Додайте цей рядок
     path('view_cart', view_cart, name='view_cart'),
     path('place_order', place_order, name='place_order'),
]
