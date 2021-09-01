"""Error handling with the `Result` type.

`Result` is an enum with the variants `Ok` and `Error`. `Ok` represents success and contains
an object. `Error` represents an error and also contains an object.
"""
from typing import Any


class Ok:
    content: str

    def __init__(self, content: Any) -> None:
        self.content: Any = content


class Error:
    def __init__(self, content: Any) -> None:
        self.content: Any = content


class Result:
    Ok: Ok
    Error: Error

    def __init__(self, result: Any) -> None:
        if isinstance(result, Ok):
            self.Ok = result
        elif isinstance(result, Error):
            self.Error = result
        else:
            raise NotImplementedError("The result only takes an Ok or Error")

    def is_ok(self) -> bool:
        """Returns true if the `Result` contains the `Ok` enum.

        Returns:
            bool: Indicates if the result was successful.
        """
        if hasattr(self, "Ok"):
            return True

        return False

    def is_err(self) -> bool:
        """Returns true if the `Result` contains the `Error` enum.

        Returns:
            bool: Indicates if the result was a failure.
        """
        if hasattr(self, "Error"):
            return True

        return False

    def get_content(self) -> Any:
        """Returns the content that is in the `Ok` or `Error` enum.

        This is useful for further result handling.

        Returns:
            Any: Returns the content of the enums.
        """
        if hasattr(self, "Ok"):
            return self.Ok.content

        return self.Error.content
