from openstack import exceptions, proxy
from openstack.reservation.v1 import floatingip, host, lease, network


class Proxy(proxy.Proxy):
    _resource_registry = {
        "host": host.Host,
        "allocation": host.HostAllocation,
        "lease": lease.Lease,
    }

    # Leases

    def get_lease(self, lease_id):
        return self._get(lease.Lease, lease_id)

    def leases(self, **query):
        """Retrieve a generator of leases."""

        return self._list(lease.Lease, **query)

    # Baremetal Hosts

    def get_host(self, host_id):
        return self._get(host.Host, host_id)

    def hosts(self, **query):
        """Retrieve a generator of reservation hosts."""

        return self._list(host.Host, **query)

    # Host allocations
    def get_allocation_for_host(self, host_id):
        return self._get(host.HostAllocation, id=host_id)

    def host_allocations(self, **query):
        """Retrieve a generator of allocations."""
        return self._list(host.HostAllocation, **query)

    # host properties

    def host_properties(self, **query):
        return self._list(host.HostProperty, **query)

    # floatingIPs

    def floatingips(self, **query):
        return self._list(floatingip.FloatingIP, **query)

    def get_floatingip(self, fip_id):
        return self._get(floatingip.FloatingIP, fip_id)

    # networks

    def networks(self, **query):
        return self._list(network.Network, **query)

    def get_network(self, network_id):
        return self._get(network.Network, network_id)

    def get_allocation_for_network(self, network_id):
        return self._get(network.NetworkAllocation, id=network_id)

    def network_allocations(self, **query):
        """Retrieve a generator of allocations."""
        return self._list(network.NetworkAllocation, **query)

    def network_properties(self, **query):
        return self._list(network.NetworkProperty, **query)
