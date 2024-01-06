from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def handleRequest (request):
    print(request)
    return JsonResponse({
        "data": "Jilo Billionaire"
    })