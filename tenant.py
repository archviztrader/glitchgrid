import uuid, os
def get_tenant_id() -> str:
    """FIXME: later read from JWT / header"""
    return os.getenv("GLITCHGRID_TENANT", "demo")
