from openstack import exceptions, resource, utils


class FloatingIP(resource.Resource):
    resource_key = "floatingip"
    resources_key = "floatingips"
    base_path = "/floatingips"

    allow_create = True
    allow_fetch = True
    allow_delete = True
    allow_list = True

    id = resource.Body("id")

    floating_network_id = resource.Body("floating_network_id")
    subnet_id = resource.Body("subnet_id")
    floating_ip_address = resource.Body("floating_ip_address")
    reservable = resource.Body("reservable")

    created_at = resource.Body("created_at")
    updated_at = resource.Body("updated_at")

    # blazar capabilities/properties are returned at the "base" level as arbitrary
    # key/value pairs. Handle this by storing all unknown keys under "properties"
    properties = resource.Body("properties")
    _store_unknown_attrs_as_properties = True
