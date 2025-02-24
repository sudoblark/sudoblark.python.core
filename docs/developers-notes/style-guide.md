# Style Guide
This document gives coding conventions for developers whom wish to
contribute to the project, or very curious end-users intending to understand
how the underlying nuts and bolts fit together.

## PEP-8

In general, [pep-8](https://peps.python.org/pep-0008/) is utilised, and is - for the most part -
automated via:
- A pre-commit hook that runs `black` across the codebase
- A commit-to-pull-request workflow that'll tell you off if you commit non-compliant code

## Type hinting

Type hinting should be used for all I/O and variables. A basic example are
provided below to assist:

```python
a: int = 1
b: int = 2
c : int = a + b
print(c)
```

## Docstrings

All docstrings should use the google format, in order to be compatible with mkdocs.

An example is given below, which also expands on type hinting for enums and classes:

```python
"""
This module defines objects in order to interact with yummy potatoes.
"""

from typing import Literal

PotatoTypes = Literal[
    "Maris Piper",
    "King Edward",
    "Jersey Royal"
]
"""
Types of potatoes known to man
"""


class Potatoes:
    """Representation of a real-world Potato
    """
    def __init__(self, variant: PotatoTypes):
        self.potato_variant = variant #: What kind of potato this is
    
    def cook(self, cook_time: int) -> bool:
        """
        Cook the yummy potato
        
        Args:
            cook_time (int): How long to cook the potato for in seconds
        Returns:
            bool: If the potato was successfully cooked
        """
        twenty_minutes_in_seconds = 1200
        if cook_time >= twenty_minutes_in_seconds:
            return True
        else:
            return False
```