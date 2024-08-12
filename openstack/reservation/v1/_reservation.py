# Apache 2 header omitted for brevity

from openstack import resource


class Lease(resource.Resource):
    resource_key = "lease"
    resources_key = "leases"
    base_path = "/leases"


class Host(resource.Resource):
    resource_key = "host"
    resources_key = "hosts"
    base_path = "/os-hosts"

    allow_create = True
    allow_fetch = True
    allow_delete = True
    allow_list = True
    allow_head = True
    allow_commit = False

    id = resource.Body("id")
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
    extra_capability = resource.Body("extra_capability")


class Allocation(resource.Resource):
    pass
