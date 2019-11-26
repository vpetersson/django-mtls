from django.db import models


class RemoteNode(models.Model):
    node_fqdn = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, default='')
    enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
