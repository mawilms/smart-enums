from smart_enums.result import Result, Ok, Error
import pytest


class TestResultCreation:
    def test_ok(self):
        result = Result(Ok("Query successful"))
        assert hasattr(result, "Ok")

    def test_error(self):
        result = Result(Error("Query failed"))
        assert hasattr(result, "Error")

    def test_unknown_object(self):
        with pytest.raises(NotImplementedError):
            Result("hello")


class TestIsOk:
    def test_is_ok_pos(self):
        result = Result(Ok("Query successful"))

        assert result.is_ok() is True

    def test_is_ok_neg(self):
        result = Result(Error("Query failed"))

        assert result.is_ok() is False


class TestIsErr:
    def test_is_err_pos(self):
        result = Result(Error("Query failed"))

        assert result.is_err() is True

    def test_is_err_neg(self):
        result = Result(Ok("Query successful"))

        assert result.is_err() is False


class TestGetContent:
    def test_ok_get_content_string(self):
        result = Result(Ok("Query successful"))

        assert result.get_content() == "Query successful"

    def test_error_get_content_string(self):
        result = Result(Error("Query failed"))

        assert result.get_content() == "Query failed"
