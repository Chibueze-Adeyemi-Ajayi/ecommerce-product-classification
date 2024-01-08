from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from . import app

@csrf_exempt
@require_http_methods(["POST"])
def handleRequest (request):

    text = request.POST.get("description")
    token = app.pipeline.processText(text)
    vector = app.pipeline.textToVec(token)
    
    clf = app.nlp.classify(vector)

    return JsonResponse({
        "data": clf[0],
       # "accuracy": app.nlp.getAccuracy(clf)
    }) 