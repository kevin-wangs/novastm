"""Module 6: feat: implement main engine."""

class Component6:
    """Implementation of component 6."""

    def __init__(self, config=None):
        self.config = config or {}
        self._initialized = False

    def initialize(self):
        self._initialized = True
        return self

    def process(self, data):
        if not self._initialized:
            raise RuntimeError("Not initialized")
        return data

    def __repr__(self):
        return f"Component6(initialized={self._initialized})"
