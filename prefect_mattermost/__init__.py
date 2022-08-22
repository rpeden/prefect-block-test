from . import _version
from .notifications import MattermostWebhook

__all__ = ["MattermostWebhook"]

__version__ = _version.get_versions()["version"]
