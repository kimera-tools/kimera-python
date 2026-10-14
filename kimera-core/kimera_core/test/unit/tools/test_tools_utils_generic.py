import unittest

from kimera_core.components.tools.utils.generic import DictUtils, NumberUtils


class TestToolsUtilsGeneric(unittest.TestCase):

    def tearDown(self) -> None:
        self._testMethodDoc = f"{self.__dict__['_testMethodName']}"
        print(self.shortDescription())

    def test_given_nested_dicts_when_advanced_update_then_merge_keys_recursively(self):
        old_object = {"a": 1, "b": {"c": 2, "d": 3}}
        new_object = {"b": {"d": 4, "e": 5}, "f": 6}
        result = DictUtils.advanced_update(old_object, new_object)
        assert (result == {"a": 1, "b": {"c": 2, "d": 4, "e": 5}, "f": 6})

    def test_given_tree_when_assign_nested_keys_then_create_missing_levels(self):
        tree = DictUtils.tree()
        tree["a"]["b"]["c"] = 1
        assert (tree["a"]["b"]["c"] == 1)

    def test_given_numbers_when_check_type_then_return_expected_flags(self):
        assert (NumberUtils.is_number(1) and NumberUtils.is_number(1.5) and NumberUtils.is_number(1j))
        assert (NumberUtils.is_int(1) and not NumberUtils.is_int(1.5))
        assert (NumberUtils.is_float(1.5) and NumberUtils.is_complex(1j))
        assert (not NumberUtils.is_number("1"))
