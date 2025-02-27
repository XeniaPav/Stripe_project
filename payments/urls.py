from django.urls import path
from payments.apps import PaymentsConfig

app_name = PaymentsConfig.name

from payments.views import ItemDetailView, buy_item

urlpatterns = [
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="detail_items"),
]
