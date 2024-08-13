from openstack import resource
from openstack.reservation.v1.common import (
    Reservation,
)


class LeaseEvent(resource.Resource):
    """Blazar lease event object.
    Can only be fetched as part of lease queries.
    """

    id = resource.Body("id")
    lease_id = resource.Body("lease_id")
    status = resource.Body("status")
    event_type = resource.Body("event_type")
    time = resource.Body("time")
    created_at = resource.Body("created_at")
    updated_at = resource.Body("updated_at")


class Lease(resource.Resource):
    resource_key = "lease"
    resources_key = "leases"
    base_path = "/leases"

    allow_create = True  # POST to /leases
    allow_fetch = True  # GET to /leases/{lease_id}
    allow_delete = True  # DELETE to /leases/{lease_id}
    allow_list = True  # GET to /leases
    allow_commit = True  # PUT to /leases/{lease_id}
    allow_head = False  # not used in API
    allow_patch = False  # PUT is used instead

    id = resource.Body("id")
    name = resource.Body("name")
    start_date = resource.Body("start_date")
    end_date = resource.Body("end_date")
    status = resource.Body("status")
    degraded = resource.Body("degraded")
    user_id = resource.Body("user_id")
    project_id = resource.Body("project_id")
    trust_id = resource.Body("trust_id")
    created_at = resource.Body("created_at")
    updated_at = resource.Body("updated_at")

    reservations = resource.Body(
        "reservations",
        type=list,
        list_type=Reservation,
        default=[],
    )

    events = resource.Body(
        "events",
        type=list,
        list_type=LeaseEvent,
        default=[],
    )
