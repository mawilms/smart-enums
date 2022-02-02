"""The `Option` type represents an optional value. An Option is either Some, which contains a value or Nothing, which doesn't.
    """
from typing import Any


class Some:
    content: str

    def __init__(self, content: Any) -> None:
        self.content: Any = content


class Nothing:
    pass


class Option:
    Some: Some
    Nothing: Nothing

    def __init__(self, option: Any) -> None:
        if isinstance(option, Some):
            self.Some = option
        elif isinstance(option, Nothing):
            self.Nothing = option
        elif hasattr(option, "__name__") and option.__name__ == "Nothing":
            self.Nothing = option
        else:
            raise NotImplementedError(
                "Option only takes a Some or Nothing object")

    def is_some(self) -> bool:
        """Returns true if the `Option` contains the `Some` enum.

        Returns:
            bool: Returns true if the Some value contains a value.
        """
        if hasattr(self, "Some"):
            return True

        return False

    def is_nothing(self) -> bool:
        """Returns true if the `Option` contains the `Nothing` enum.

        Returns:
            bool: Returns true if the `Option` is a `Nothing` value.
        """
        if hasattr(self, "Nothing"):
            return True

        return False

    def get_content(self) -> Any:
        """Returns the content of the `Some` value.

        Returns:
            Any: Returns the content of `Some`
        """
        if hasattr(self, "Some"):
            return self.Some.content

        return None

    def unwrap(self):
        if hasattr(self, "Some"):
            return self.Some.content

        raise WrongOptionException(f"Option doesn't contain anything")


class WrongOptionException(Exception):
    pass
