import pkg_resources

__version__ = pkg_resources.get_distribution("zerxis-invitations").version
default_app_config = "zerxis_invitations.invitations.apps.AppConfig"
