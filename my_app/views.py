from django.http import JsonResponse

import logging

logger = logging.getLogger()

def index(request):
    logger.error('** my error!')
    return JsonResponse({ 'msg': 'Hi!' })
