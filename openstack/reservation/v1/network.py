from openstack import exceptions, resource, utils
from openstack.reservation.v1.common import AllocReservation


class Network(resource.Resource):
    resource_key = "network"
    resources_key = "networks"
    base_path = "/networks"

    allow_create = True
    allow_fetch = True
    allow_delete = True
    allow_list = True

    id = resource.Body("id")

    network_type = resource.Body("network_type")
    physical_network = resource.Body("physical_network")
    segment_id = resource.Body("segment_id")

    created_at = resource.Body("created_at")
    updated_at = resource.Body("updated_at")

    # these are defined ad-hoc py the properties API, and so will be shown under properties if present
    # stitch_provider = resource.Body("stitch_provider")
    # usage_type = resource.Body("usage_type")

    # blazar capabilities/properties are returned at the "base" level as arbitrary
    # key/value pairs. Handle this by storing all unknown keys under "properties"
    properties = resource.Body("properties")
    _store_unknown_attrs_as_properties = True


class NetworkAllocation(resource.Resource):
    resource_key = "allocation"
    resources_key = "allocations"
    base_path = "/networks/allocations"

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
        url = utils.urljoin(Network.base_path, resource_id, "allocation")
        return super().fetch(
            session,
            requires_id=False,
            base_path=url,
        )


class NetworkProperty(resource.Resource):
    resource_key = "resource_property"
    resources_key = "resource_properties"
    base_path = "/networks/properties"

    allow_list = True  # GET to v1/networks/properties
    allow_patch = True  # PATCH to v1/networks/properties/{property_name}

    _query_mapping = resource.QueryParameters(
        "detail",
        "all",
    )

    property = resource.Body("property", alternate_id=True)
    private = resource.Body("private")
    values = resource.Body("values")

    properties = resource.Body("properties")
    _store_unknown_attrs_as_properties = True
