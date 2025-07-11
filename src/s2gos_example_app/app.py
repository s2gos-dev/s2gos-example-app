import importlib

from s2gos_server.services.local import LocalService

from . import processes

service = LocalService(
    title="S2GOS App example",
    description="Generic S2GOS app example.",
)

for process in processes.__all__:
    print(__name__)

    importlib.import_module(f".processes.{process}", __package__)
