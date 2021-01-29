from django.conf import settings  # noqa

from appconf import AppConf


class ZerxisInvitationsAppConf(AppConf):

    DEFAULT_EXPIRATION = 168
    DEFAULT_INVITE_ALLOCATION = 0

    class Meta:
        prefix = "zerxis_invitations"
