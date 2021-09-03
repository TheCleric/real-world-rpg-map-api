import base64
import json
from xml.etree import ElementTree

import pytest

from api import main

@pytest.mark.asyncio
async def test_hello() -> None:
    map_result = {}

    with pytest.warns(DeprecationWarning):
        map_result_response = main.create_map()
        map_result_iterator = [x async for x in map_result_response.body_iterator]
        map_result = json.loads("".join(map_result_iterator))
    assert 'map' in map_result

    generated_map = map_result['map']
    assert generated_map is not None and len(generated_map) > 0

    decoded = base64.b64decode(generated_map).decode('utf-8')
    assert decoded is not None

    map_xml = ElementTree.fromstring(decoded)
    assert map_xml is not None

    assert map_xml.tag == '{http://www.w3.org/2000/svg}svg'

if __name__ == '__main__':
    test_hello()
