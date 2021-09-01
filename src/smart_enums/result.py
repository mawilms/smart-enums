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
        if hasattr(self, "Ok"):
            return True

        return False

    def is_err(self) -> bool:
        if hasattr(self, "Error"):
            return True

        return False

    def get_content(self) -> Any:
        if hasattr(self, "Ok"):
            return self.Ok.content

        return self.Error.content
