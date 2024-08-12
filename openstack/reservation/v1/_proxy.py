from openstack import exceptions, proxy
from openstack.reservation.v1 import _reservation


class Proxy(proxy.Proxy):
    _resource_registry = {
        "host": _reservation.Host,
        "allocation": _reservation.Allocation,
        "lease": _reservation.Lease,
    }

    def hosts(self, **query):
        """Retrieve a generator of reservation hosts."""

        return _reservation.Host.list(self, **query)

    def get_host(self, host_id):
        """Retrieve a generator of reservation hosts."""

        return _reservation.Host.get(self, host_id)
