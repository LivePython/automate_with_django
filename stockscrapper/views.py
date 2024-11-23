from django.shortcuts import render
from dal import autocomplete
from .models import Stock
from .forms import StockForm


# Create your views here.
def scrape_stock(request):
    form = StockForm()
    context = {
        'form': form,
    }
    return render(request, 'stockscrapper/stocks.html', context=context)    


class StockAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Stock.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs