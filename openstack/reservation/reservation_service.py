from openstack import service_description
from openstack.reservation.v1 import _proxy as _proxy_v1


class ReservationService(service_description.ServiceDescription):
    """The reservation service."""

    supported_versions = {
        "1": _proxy_v1.Proxy,
    }
