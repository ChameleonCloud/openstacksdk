from openstack import resource
from openstack.reservation.v1.common import Reservation


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


class HostAllocation(resource.Resource):
    resource_key = "allocation"
    resources_key = "allocations"
    base_path = "/os-hosts/allocations"

    allow_create = True
    allow_fetch = True
    allow_delete = True
    allow_list = True
    allow_head = True
    allow_commit = False

    resource_id = resource.Body("resource_id", alternate_id=True)
    reservations = resource.Body(
        "reservations",
        type=list,
        list_type=Reservation,
        default=[],
    )
