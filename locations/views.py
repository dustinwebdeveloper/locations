from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def locations(request):
    if request.method != 'POST':
        return JsonResponse({
            "error_message": "Just Post is Allowed"
            }, status=405)
    data = {}
    return JsonResponse(data, status=200)