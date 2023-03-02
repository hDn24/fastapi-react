import random

# from app.utils import random_string
import utils


class TestRandomString:
    def test_length(self):
        length = random.randint(1, 100)
        str1 = utils.random_string(length)
        # sanity check
        assert length == len(str1)

    def test_different_each_time(self):
        str1 = utils.random_string(5)
        str2 = utils.random_string(5)
        # check two calls return different strings
        assert 2 == len(set([str1, str2]))
