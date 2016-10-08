"""
AsyncFunctionDef astroid node

Subclass of FunctionDef astroid node. An async def function definition and used
for async astroid nodes like AsyncFor and AsyncWith.

Attributes:
    - name        (str)
        - The function's name.
    - args        (Arguments)
        - An arguments node. See Arguments.py for more details.
    - doc         (str)
        - The docstring of the function.
    - body        (List[Node])
        - The list of nodes inside the function.
    - decorators  (Decorator)
        - The decorator to be applied on this function.
    - returns     (None)
        - The return annotation.

Example:
    - name        -> "func"
    - args        -> arg
    - doc         -> "This is function animal."
    - body        -> [Assign(dog, "an animal")]
    - decorators  -> @wrapper
    - returns     -> return dog
"""

@wrapper
def animal(arg):
    """
    This is function animal.
    """
    dog = "an animal"
    return dog
