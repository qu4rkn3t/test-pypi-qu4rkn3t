"""Core functionality for the example package."""

def greet(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"
