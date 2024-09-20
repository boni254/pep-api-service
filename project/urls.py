from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView

from app.core.apis import SpectacularElementsView

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/doc/", SpectacularElementsView.as_view(url_name="schema"), name="elements-ui"),
    path("api/anamnese/", include("app.anamnese.urls")),
    path("api/evolucao/", include("app.evolucao.urls")),
    path("api/receituario/", include("app.receituario.urls")),
]
