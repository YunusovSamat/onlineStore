from catalogApp.models import Subcatalog
from productApp.models import Product


def get_subcatalog_state(request):
    def get_subcatalog(id_catalog, flag=False):
        arr = []
        clothes = Subcatalog.objects.filter(fk_catalog_id=id_catalog)
        for x in clothes:
            if flag:
                products = Product.objects.filter(fk_subcatalog_id=x, new=True)
            else:
                products = Product.objects.filter(fk_subcatalog_id=x, old_price__gt=0)

            if products:
                arr.append((x.id, x.name))
        return arr

    context = {
        'clothes_sale': get_subcatalog('1'),
        'shoes_sale': get_subcatalog('2'),
        'accessories_sale': get_subcatalog('3'),
        'clothes_new': get_subcatalog('1', True),
        'shoes_new': get_subcatalog('2', True),
        'accessories_new': get_subcatalog('3', True),

    }

    return context
