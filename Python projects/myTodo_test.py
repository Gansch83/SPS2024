import unittest
from myTodo_bib import Note, Task, MyList

class TestMyList(unittest.TestCase):
    def setUp(self):
        """Set up a fresh MyList instance before each test."""
        self.my_list = MyList()

    def test_add_item(self):
        note = Note(1, "open", "Test Note")
        self.my_list.add_item(note)
        self.assertEqual(len(self.my_list.items), 1)
        self.assertEqual(self.my_list.items[0].desc, "Test Note")

    def test_remove_item(self):
        note = Note(1, "open", "Test Note")
        self.my_list.add_item(note)
        self.my_list.remove_item(0)
        self.assertEqual(len(self.my_list.items), 0)

    def test_view_item(self):
        note = Note(1, "open", "Test Note")
        self.my_list.add_item(note)
        # Assuming view_item prints items, you can capture stdout if needed.

    def test_set_item_done(self):
        note = Note(1, "open", "Test Note")
        self.my_list.add_item(note)
        self.my_list.set_item_done(0)
        self.assertEqual(self.my_list.items[0].status, "done")

    def test_save_and_load(self):
        note = Note(1, "open", "Test Note")
        self.my_list.add_item(note)
        self.my_list.save_to_file("myTodo_unittest.csv")

        new_list = MyList()
        new_list.load_from_file("myTodo_unittest.csv")
        self.assertEqual(len(new_list.items), 1)
        self.assertEqual(new_list.items[0].desc, "Test Note")

if __name__ == "__main__":
    unittest.main()