from wheke import Pod, ServiceConfig

from .routes import router
from .service import EntryService, entry_service_factory

entry_pod = Pod(
    "entry",
    services=[ServiceConfig(EntryService, entry_service_factory)],
    router=router,
)
