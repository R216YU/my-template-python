from src.utils.feeling import get_random_feeling


class TestGetFeeling:
    def test_return_type(self):
        result = get_random_feeling()

        assert isinstance(result, str)
