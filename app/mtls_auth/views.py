import re
from django.http import JsonResponse
from .models import RemoteNode


def access_denied():
    payload = {'msg': 'Access Denied'}
    return JsonResponse(payload, status=401)


def index(request):
    # For debugging
    for h in request.META:
        print(h)

    if not request.META.get('HTTP_SSL_CLIENT_VERIFY') == 'SUCCESS':
        access_denied()

    # Extract Certificate
    matchObj = re.match(
        r'.*CN=(.*.d.wott.local)',
        request.META.get('HTTP_SSL_CLIENT'),
        re.M | re.I
    )

    print('Got request from {}'.format(matchObj.group(1)))

    try:
        RemoteNode.objects.filter(node_fqdn=matchObj.group(1), enabled=True)
        payload = {'hello': matchObj.group(1)}
        return JsonResponse(payload, status=200)
    except RemoteNode.DoesNotExist:
        access_denied()
