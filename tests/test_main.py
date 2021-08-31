from api import main


def test_hello() -> None:
    map_result = main.create_map()
    assert "map" in map_result
    assert len(map_result["map"]) > 100

if __name__ == "__main__":
    test_hello()
