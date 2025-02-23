# Sudoblark Core Python library

This is a core library, written in Python, to provide a good, known, fully unit tested
working class library to assist Sudoblark in code writing activities.

Public interfaces are exported for interaction with various RESTAPIs.

For effective usage of the library, it is recommended to configure logging in order to receive
additional information regarding library operations:
```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(name)s - %(asctime)s - %(message)s')
```

See links on the left for details about the basic operating principles of
the library, and for documentation on all known interfaces.