import pytest

from api_client import APIClient
from data_objects import HotelSearchData


@pytest.fixture(scope="class")
def api_client(config_reader):
    base_url = config_reader.get("General", "base_url")
    return APIClient(base_url)


@pytest.mark.api
class TestAPI:
    def test_get_hotels(self, api_client):
        response = api_client.get_hotels()
        assert response.status_code == 200
        assert "hotels" in response.json()

    def test_search_hotels(self, api_client):
        search_data = HotelSearchData("2023-08-20", "2023-08-25", 2)
        response = api_client.search_hotels(search_data)
        assert response.status_code == 200
        assert "results" in response.json()
