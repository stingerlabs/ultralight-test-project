import pytest
from bad_hash_table import BadHashTable

def test_insert(record_xml_attribute):
    record_xml_attribute("name", "VER-1 test insert success")
    hash_table = BadHashTable()
    hash_table.insert('hello', 'world')
    result = hash_table.get('hello')
    assert result == 'world'


def test_get_wrong_key(record_xml_attribute):
    record_xml_attribute("name", "VER-2 test getting incorrect key raises error")
    hash_table = BadHashTable()
    hash_table.insert('hello', 'world')
    with pytest.raises(Exception):
        hash_table.get('world')

# def test_getting_correct_key_raises_exception(record_xml_attribute):
#     record_xml_attribute("name", "VER-3 test getting correct key raises exception (this will always fail)")
#     hash_table = BadHashTable()
#     hash_table.insert('hello', 'world')
#     with pytest.raises(Exception):
#         hash_table.get('hello')