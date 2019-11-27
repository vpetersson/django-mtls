from django.contrib import admin
from .models import RemoteNode


class RemoteNodeAdmin(admin.ModelAdmin):
    model = RemoteNode

    list_display = [
        'node_fqdn',
        'comment',
        'enabled',
        'created_at',
    ]

    list_filter = (
        'enabled',
    )

    ordering = (
        'node_fqdn',
    )


admin.site.register(RemoteNode, RemoteNodeAdmin)
