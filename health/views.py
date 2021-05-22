from django.http import JsonResponse
from datetime import datetime, timezone
import time

# Create your views here.
def health(request):
    local_time = datetime.now(timezone.utc).astimezone()
    data = {'time': local_time.isoformat()}
    return JsonResponse(data, status=200)