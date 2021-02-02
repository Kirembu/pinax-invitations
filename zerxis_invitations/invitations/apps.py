import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "zerxis_invitations"
    label = "zerxis_invitations"
    verbose_name = _("Zerxis Invitations")

    def ready(self):
        importlib.import_module("zerxis_invitations.invitations.receivers")
