from django.conf.urls import include, url

urlpatterns = [
    url(r"^account", include("zerxis_account.urls")),
    url(r"^", include("zerxis.invitations.urls", namespace="zerxis_invitations")),
]
