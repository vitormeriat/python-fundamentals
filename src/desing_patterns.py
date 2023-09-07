from functools import wraps


class MaxTriesExceededError(Exception):
    pass


class MyTry:
    def tries(max_tries=3, error_message="failure"):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for try_count in range(max_tries):
                    try:
                        return func(*args, **kwargs)
                    except Exception:
                        pass
                raise MaxTriesExceededError(error_message)

            return wrapper

        return decorator


class Decorator:

    def __init__(self) -> None:
        pass

    def make_blink(function):
        """Defines the decorator"""

        # This makes the decorator transparent in terms of its name and docstring
        @wraps(function)
        def decorator():
            # Grab the return value of the function being decorated
            ret = function()

            # Add new functionality to the function being decorated
            return f"<blink>{ret}</blink>"

        return decorator

# Apply the decorator here!


@Decorator.make_blink
def hello_world():
    """Original function! """

    return "Hello, World!"


# Check the result of decorating
print(hello_world())

# Check if the function name is still the same name of the function being decorated
print(hello_world.__name__)

# Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)
