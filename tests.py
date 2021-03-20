import unittest
import shutil
import funcs_4_tests as fs


class Test1Class(unittest.TestCase):
    def test_bool(self):
        n1, n2, n3 = 4, 5, -8
        s1 = fs.add(n1, n2)
        s2 = fs.add(n1, n3)
        self.assertTrue(s1 >= n1)
        self.assertFalse(s2 >= n1)
        for i in range(-5, 1):
            with self.subTest(i=i):
                # some failures to be shown
                self.assertTrue(fs.add(i, 1) > 0)
                self.assertGreater(s1, s2)

    def test_is_in(self):
        set1, set2 = {1, 34, 55}, {52, 34, 1111}
        intersection = fs.intersect(set1, set2)
        self.assertIn(34, intersection)
        self.assertNotIn(1, intersection)

    def test_greater_less(self):
        str1, str2 = 'abcd', 'efgh'
        extended = fs.extend_line(str1, str2)
        self.assertLess(len(str1), len(extended))
        self.assertGreater(len(extended), len(str2))

    def test_equality(self):
        l1, l2 = ['a', 'b', 'c', 'd'], ['d', 'c', 'k']
        self.assertCountEqual(l1, fs.change_common_elements(l1, l2))


class Test2Class(unittest.TestCase):
    def setUp(self) -> None:
        fs.new_folder_w_f('C:\\Users\\a.zasypkin\\PycharmProjects\\python_2-2\\test text\\')

    def test_the_text(self):
        with open('test text\\test.txt', 'r') as f:
            txt = f.read()
            self.assertTrue(len(txt) != 0 and txt == 'some stuff')

    def tearDown(self) -> None:
        shutil.rmtree('C:\\Users\\a.zasypkin\\PycharmProjects\\python_2-2\\test text\\')


if __name__ == '__main__':
    unittest.main()
