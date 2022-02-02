from smart_enums.option import Nothing, Option, Some, WrongOptionException
import pytest


class TestOptionCreation:
    def test_some(self):
        option = Option(Some("Query successful"))
        assert hasattr(option, "Some")

    def test_nothing(self):
        option = Option(Nothing())
        assert hasattr(option, "Nothing")

    def test_nothing_class(self):
        option = Option(Nothing)
        assert hasattr(option, "Nothing")

    def test_unknown_object(self):
        with pytest.raises(NotImplementedError):
            Option("hello")


class TestIsSome:
    def test_is_some_pos(self):
        option = Option(Some("Query successful"))

        assert option.is_some() is True

    def test_is_some_neg(self):
        option = Option(Nothing())

        assert option.is_some() is False


class TestIsNothing:
    def test_is_nothing_pos(self):
        option = Option(Nothing())

        assert option.is_nothing() is True

    def test_is_nothing_class(self):
        option = Option(Nothing)

        assert option.is_nothing() is True

    def test_is_nothing_neg(self):
        option = Option(Some("Query failed"))

        assert option.is_nothing() is False


class TestGetContent:
    def test_some_get_content(self):
        option = Option(Some("Query successful"))

        assert option.get_content() == "Query successful"

    def test_nothing_get_content(self):
        option = Option(Nothing())

        assert option.get_content() is None


class TestUnwrap:
    def test_some_unwrap(self):
        option = Option(Some("Query successful"))

        assert option.unwrap() == "Query successful"

    def test_nothing_unwrap(self):
        option = Option(Nothing())

        with pytest.raises(WrongOptionException):
            option.unwrap()
