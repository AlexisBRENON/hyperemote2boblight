import pytest
import hyperemote2boblight.lib.priority_list as priority_list

class TestPriorityList:

  @pytest.fixture
  def empty_priority_list(self):
    return priority_list.PriorityList();

  
  def test_empty_list_get(self, empty_priority_list):
    assert empty_priority_list.get_first() == (None, None)

  # def test_empty_list_set(self, empty_priority_list):
  #   assert 0

  # def test_empty_list_clear(self, empty_priority_list):
  #   assert 0

  # def test_list_get(self, non_empty_priority_list):
  #   assert 0

  # def test_list_set(self, non_empty_priority_list):
  #   assert 0

  # def test_list_clear(self, non_empty_priority_list):
  #   assert 0

  