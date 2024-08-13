from openstack.reservation.v1 import lease
from openstack.tests.unit import base


class TestLease(base.TestCase):
    def setUp(self):
        super().setUp()

    def test_basic(self):
        leases_resource = lease.Lease()
        self.assertEqual("lease", leases_resource.resource_key)
        self.assertEqual("leases", leases_resource.resources_key)
        self.assertEqual("/leases", leases_resource.base_path)
        self.assertTrue(leases_resource.allow_create)
        self.assertTrue(leases_resource.allow_fetch)
        self.assertTrue(leases_resource.allow_delete)
        self.assertTrue(leases_resource.allow_list)
        self.assertTrue(leases_resource.allow_commit)

        self.assertFalse(leases_resource.allow_head)
        self.assertFalse(leases_resource.allow_patch)

        self.assertEqual("POST", leases_resource.create_method)
        self.assertEqual("PUT", leases_resource.commit_method)
