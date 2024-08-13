from openstack import resource


class Reservation(resource.Resource):
    """Blazar reservation object.
    Can only be fetched as part of lease or allocation queries.
    """

    id = resource.Body("id")
    lease_id = resource.Body("lease_id")
    status = resource.Body("status")
    missing_resources = resource.Body("missing_resources")
    resources_changed = resource.Body("resources_changed")
    resource_id = resource.Body("resource_id")
    created_at = resource.Body("created_at")
    updated_at = resource.Body("updated_at")

    resource_type = resource.Body("resource_type")

    # each blazar plugin defines a new type of reservation object,
    # which may have additional fields. Store those extra fields under "properties"
    properties = resource.Body("properties")
    _store_unknown_attrs_as_properties = True


class HostReservation(Reservation):
    # from physical:host

    resource_properties = resource.Body("resource_properties", type=str)
    min = resource.Body("min", type=int)
    max = resource.Body("max", type=int)
    hypervisor_properties = resource.Body("hypervisor_properties")
    before_end = resource.Body("before_end")


class InstanceReservation(Reservation):
    # from virtual:instance

    resource_properties = resource.Body("resource_properties", type=str)
    amount = resource.Body("amount")
    vcpus = resource.Body("vcpus")
    memory_mb = resource.Body("memory_mb")
    disk_gb = resource.Body("disk_gb")
    affinity = resource.Body("affinity")
    flavor_id = resource.Body("flavor_id")
    server_group_id = resource.Body("server_group_id")
    aggregate_id = resource.Body("aggregate_id")


class FloatingIPReservation(Reservation):
    network_id = resource.Body("network_id")
    amount = resource.Body("amount")
    required_floatingips = resource.Body("required_floatingips")
