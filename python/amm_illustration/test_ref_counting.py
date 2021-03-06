'illustrate reference counting'
import sys
import unittest


class Foo:
  pass


class TestRefCount(unittest.TestCase):
  'Fun with ref counts'

  def test_no_explicit_reference_has_refcount(self):

    self.assertEqual(1, sys.getrefcount(Foo()))

  def test_one_explicit_reference_has_refcount(self):

    first = Foo()

    self.assertEqual(None, sys.getrefcount(first))

  def test_two_explicit_references_has_refcount(self):

    first = Foo()
    second = first  # second and first both point to the same instance of Foo

    self.assertEqual(None, sys.getrefcount(first))
    self.assertEqual(None, sys.getrefcount(second))

  def test_redefined_explicit_reference_has_refcount(self):

    first = Foo()
    second = first
    self.assertEqual(None, sys.getrefcount(first))
    self.assertEqual(None, sys.getrefcount(second))

    second = Foo()  # second now points to a difference instance of Foo
    self.assertEqual(None, sys.getrefcount(first))
    self.assertEqual(None, sys.getrefcount(second))

  def test_internal_object_has_many_references(self):

    none = None
    self.assertEqual(None, sys.getrefcount(none))


if __name__ == '__main__':
  unittest.main(verbosity=2)
