import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from payments.models import Item
from config.settings import STRIPE_API_KEY_SECRET_KEY, STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY_SECRET_KEY
class ItemDetailView(DetailView):
    """Просмотр информации о конкретном товаре"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_API_KEY_SECRET_KEY'] = STRIPE_API_KEY_SECRET_KEY
        return context

    model = Item
    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


def buy_item(request, id):
    """ Оплата товара """
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),  # цена в центах
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )
    return redirect(session.url)