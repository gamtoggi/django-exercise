from django.http import JsonResponse

import logging

logger = logging.getLogger('my_logger')

def index(request):
    logger.debug('my debug msg!')
    logger.info('my info msg!')
    logger.warning('my warning msg!')
    logger.error('my error msg!')
    logger.critical('my critical msg!')

    return JsonResponse({ 'msg': 'Hi!' })
