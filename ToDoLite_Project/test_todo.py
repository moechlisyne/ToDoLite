# test_todo.py
import unittest
import todo_module

class TestTodoLite(unittest.TestCase):
    def setUp(self):
        todo_module.tasks.clear()

    def test_add_task(self):
        result = todo_module.add_task("Belajar Python")
        self.assertIn("berhasil", result)
        self.assertEqual(len(todo_module.tasks), 1)

    def test_delete_task(self):
        todo_module.add_task("Belajar AI")
        result = todo_module.delete_task(0)
        self.assertIn("berhasil dihapus", result)

    def test_show_tasks(self):
        todo_module.add_task("Baca buku")
        output = todo_module.show_tasks()
        self.assertIn("1. Baca buku", output)

if __name__ == '__main__':
    unittest.main()