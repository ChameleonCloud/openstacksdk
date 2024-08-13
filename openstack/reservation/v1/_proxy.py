from openstack import exceptions, proxy
from openstack.reservation.v1 import host, lease


class Proxy(proxy.Proxy):
    _resource_registry = {
        "host": host.Host,
        "allocation": host.HostAllocation,
        "lease": lease.Lease,
    }

    def get_lease(self, lease_id):
        return self._get(lease.Lease, lease_id)

    def leases(self, **query):
        """Retrieve a generator of leases."""

        return self._list(lease.Lease, **query)

    def get_allocation_for_host(self, host_id):
        return self._get(host.HostAllocation, id=host_id)

    def allocations(self, **query):
        """Retrieve a generator of allocations."""

        return self._list(host.HostAllocation, **query)

    def get_host(self, host_id):
        return self._get(host.Host, host_id)

    def hosts(self, **query):
        """Retrieve a generator of reservation hosts."""

        return self._list(host.Host, **query)
