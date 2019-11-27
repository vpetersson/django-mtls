import re
from django.http import JsonResponse
from .models import RemoteNode


def index(request):
    if not request.META.get('HTTP_SSL_CLIENT_VERIFY') == 'SUCCESS':
        payload = {'msg': 'You shall not pass!'}
        return JsonResponse(payload, status=401)

    # Extract Certificate
    matchObj = re.match(
        r'.*CN=(.*.d.wott.local)',
        request.META.get('HTTP_SSL_CLIENT'),
        re.M | re.I
    )

    if RemoteNode.objects.filter(node_fqdn=matchObj.group(1), enabled=True):
        payload = {'msg': 'Welcome {}. We\'ve been expecting you.'.format(matchObj.group(1))}
        return JsonResponse(payload, status=200)

    payload = {'msg': 'You shall not pass!'}
    return JsonResponse(payload, status=401)
