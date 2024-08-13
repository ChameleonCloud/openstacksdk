from openstack import exceptions, proxy
from openstack.reservation.v1 import host, lease


class Proxy(proxy.Proxy):
    _resource_registry = {
        "host": host.Host,
        "allocation": host.HostAllocation,
        "lease": lease.Lease,
    }

    def leases(self, **query):
        """Retrieve a generator of leases."""

        return lease.Lease.list(self, **query)

    def allocations(self, **query):
        """Retrieve a generator of allocations."""

        return host.HostAllocation.list(self, **query)

    def hosts(self, **query):
        """Retrieve a generator of reservation hosts."""

        return host.Host.list(self, **query)
