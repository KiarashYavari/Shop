from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from base.models import Product
from base.serializers import ProductSerializer


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({}, status=405)

