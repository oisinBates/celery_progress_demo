from django.shortcuts import render
from django.http import HttpResponse
from .tasks import get_nasa_image
import time

# Create your views here.
def index(request):
    celery_task_ids = {i:get_nasa_image.delay(5).task_id for i in range(8)}
    return render(request, 'demo_app/index.html', context={'celery_task_ids': celery_task_ids})
