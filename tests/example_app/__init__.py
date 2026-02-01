from wheke import Wheke, WhekeSettings

from wheke_sqlmodel import sqlmodel_pod

from .pod import entry_pod


def build_wheke(settings: WhekeSettings) -> Wheke:
    wheke = Wheke(settings)

    wheke.add_pod(sqlmodel_pod)
    wheke.add_pod(entry_pod)

    return wheke
