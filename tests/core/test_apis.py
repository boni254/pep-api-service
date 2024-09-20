from app.core.apis import SpectacularElementsView


class TestSpectacularElementsViewSpectacularElementsView:
    def test_get_view(self, rf):
        view = SpectacularElementsView.as_view()

        response = view(rf.get("/api/doc/"))

        response.render()

        assert response.status_code == 200
        assert "elements-api" in response.content.decode()
