from openstack import exceptions, resource, utils
from openstack.reservation.v1.common import AllocReservation


class Device(resource.Resource):
    resource_key = "device"
    resources_key = "devices"
    base_path = "/devices"

    allow_create = True
    allow_fetch = True
    allow_delete = True
    allow_list = True
    allow_commit = True

    id = resource.Body("id")
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

    def get_allocations_for_device(self):
        if self.reservation_adapter:
            return DeviceAllocation().fetch(
                self.reservation_adapter, resource_id=self.id
            )

    def get_device_with_reservations(self):
        alloc = self.get_allocations_for_device()
        self.reservations = alloc.reservations
        return self


class DeviceAllocation(resource.Resource):
    resource_key = "allocation"
    resources_key = "allocations"
    base_path = "/devices/allocations"

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
        url = utils.urljoin(Device.base_path, resource_id, "allocation")
        return super().fetch(
            session,
            requires_id=False,
            base_path=url,
        )


class DeviceProperty(resource.Resource):
    resource_key = "resource_property"
    resources_key = "resource_properties"
    base_path = "/devices/properties"

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
