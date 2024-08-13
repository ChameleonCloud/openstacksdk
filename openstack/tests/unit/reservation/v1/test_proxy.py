from openstack.reservation.v1 import _proxy, host, lease
from openstack.tests.unit import test_proxy_base as test_proxy_base


class TestReservationBase(test_proxy_base.TestProxyBase):
    def setUp(self):
        super().setUp()
        self.proxy = _proxy.Proxy(self.session)


class TestReservationLease(TestReservationBase):
    # lease operations
    def test_lease_list(self):
        self.verify_list(self.proxy.leases, lease.Lease)

    def test_lease_get(self):
        self.verify_get(self.proxy.get_lease, lease.Lease)


class TestReservationHost(TestReservationBase):
    def test_host_list(self):
        self.verify_list(self.proxy.hosts, host.Host)

    def test_host_get(self):
        self.verify_get(self.proxy.get_host, host.Host)


class TestReservationHostAllocation(TestReservationBase):
    def test_allocation_list(self):
        self.verify_list(self.proxy.allocations, host.HostAllocation)

    def test_allocation_get(self):
        self.verify_get(self.proxy.get_allocation, host.HostAllocation)
