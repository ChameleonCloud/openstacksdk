from openstack import exceptions, resource, utils
from openstack.reservation.v1.common import AllocReservation


class Host(resource.Resource):
    resource_key = "host"
    resources_key = "hosts"
    base_path = "/os-hosts"

    allow_create = True
    allow_fetch = True
    allow_delete = True
    allow_list = True
    allow_commit = True

    allow_head = False
    allow_patch = False  # PUT is used instead

    id = resource.Body("id")
    name = resource.Body("hypervisor_hostname")
    hypervisor_hostname = resource.Body("hypervisor_hostname")
    hypervisor_type = resource.Body("hypervisor_type")
    hypervisor_version = resource.Body("hypervisor_version")
    vcpus = resource.Body("vcpus")
    cpu_info = resource.Body("cpu_info")
    memory_mb = resource.Body("memory_mb")
    local_gb = resource.Body("local_gb")
    service_name = resource.Body("service_name")
    reservable = resource.Body("reservable")
    status = resource.Body("status")
    trust_id = resource.Body("trust_id")
    created_at = resource.Body("created_at")
    updated_at = resource.Body("updated_at")

    # blazar capabilities/properties are returned at the "base" level as arbitrary
    # key/value pairs. Handle this by storing all unknown keys under "properties"
    properties = resource.Body("properties")
    _store_unknown_attrs_as_properties = True

    reservations = resource.Computed(
        "reservations",
        type=list,
        list_type=AllocReservation,
        default=[],
    )

    def __init__(self, _synchronized=False, connection=None, **attrs):
        super().__init__(_synchronized, connection, **attrs)
        self.reservation_adapter = connection.reservation

    def get_allocations_for_host(self):
        if self.reservation_adapter:
            return HostAllocation().fetch(self.reservation_adapter, resource_id=self.id)

    def get_host_with_reservations(self):
        alloc = self.get_allocations_for_host()
        self.reservations = alloc.reservations
        return self


class HostAllocation(resource.Resource):
    resource_key = "allocation"
    resources_key = "allocations"
    base_path = "/os-hosts/allocations"

    allow_list = True  # GET to v1/os-hosts/allocations
    allow_fetch = True  # GET to v1/os-hosts/{host_id}/allocation, this is under host object instead

    resource_id = resource.Body("resource_id", alternate_id=True)
    reservations = resource.Body(
        "reservations",
        type=list,
        list_type=AllocReservation,
        default=[],
    )

    def fetch(self, session, resource_id):
        url = utils.urljoin(Host.base_path, resource_id, "allocation")
        return super().fetch(
            session,
            requires_id=False,
            base_path=url,
        )


class HostProperty(resource.Resource):
    resource_key = "resource_property"
    resources_key = "resource_properties"
    base_path = "/os-hosts/properties"

    allow_list = True  # GET to v1/os-hosts/properties
    allow_patch = True  # PATCH to v1/os-hosts/properties/{property_name}

    _query_mapping = resource.QueryParameters(
        "detail",
        "all",
    )

    property = resource.Body("property", alternate_id=True)
    private = resource.Body("private")
    values = resource.Body("values")

    properties = resource.Body("properties")
    _store_unknown_attrs_as_properties = True
