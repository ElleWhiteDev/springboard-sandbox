# from unittest import TestCase
# from app import reverse_str, is_palindrome, factorial 


# class AlgorithmsTestCase(TestCase):
#     def test_reverse(self):
#         self.assertEqual(reverse_str('hello'), 'olleh')
#         self.assertEqual(reverse_str('Apple'), 'elppA')


#     def test_is_palindrome(self):
#         self.assertTrue(is_palindrome('racecar'))
#         self.assertTrue(is_palindrome('Racecar'))
#         #should ignore casing
#         self.assertTrue(is_palindrome('kayak'))
#         self.assertFalse(is_palindrome('taco'))


#     def test_factorial(self):
#         self.assertEqual(factorial(5), 120)
#         self.assertEqual(factorial(3), 6)
#         self.assertRaises(ValueError, factorial, -1) #not factorial(-1)
#         self.assertRaises(ValueError, factorial, 4.3)

#must be named test_xxxxx to run in unittest


#~~~~~~~~~~~~~~~~~~~~~~~~~integration tests~~~~~~~~~~~~~~~~~~~~
from app import app
from flask import session
from unittest import TestCase


app.config["TESTING"] = True
#makes sure that errors are shown during testing
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]
#keeps toolbar from showing up in tests


class ColorViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        print("INSIDE SETUP CLASS")

    @classmethod
    def tearDownClass(cls):
        print("INSIDE TEARDOWN CLASS")

    def setUp(self):
        """Stuff to do before every test."""
        print("INSIDE SETUP")

    def tearDown(self):
        """Stuff to do after each test."""
        print("INSIDE TEARDOWN")

    #GET request
    """Tests for status code and verified response string"""
    def test_color_form(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)

    def test_color_submit(self):
        #POST request
        """Tests for status code and verified response string"""
        with app.test_client() as client:
            res = client.post("/fav-color", data={"color": "sunshine"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(" <h3>Woah! I like sunshine, too!</h3>", html)

    def test_redirection(self):
        with app.test_client() as client:
            res = client.get("/redirect-me")

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "/")

    def test_redirection_followed(self):
        with app.test_client() as client:
            res = client.get("/redirect-me", follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)

    def test_session_count(self):
        with app.test_client() as client:
            res = client.get("/")

            self.assertEqual(res.status_code, 200)
            self.assertEqual(session["count"], 1)

    def test_session_count_set(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["count"] = 999

            res = client.get("/")

            self.assertEqual(res.status_code, 200)
            self.assertEqual(session["count"], 1000)

#python -m unittest
#python -m unittest test_app
#pyhton -m unittest test_app.ColorsViewsTestCase
#python -m unittest test_app.ColorsViewsTestCase.test_color_form