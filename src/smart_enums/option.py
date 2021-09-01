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
        if hasattr(self, "Some"):
            return True

        return False

    def is_nothing(self) -> bool:
        if hasattr(self, "Nothing"):
            return True

        return False

    def get_content(self) -> Any:
        if hasattr(self, "Some"):
            return self.Some.content

        return None
