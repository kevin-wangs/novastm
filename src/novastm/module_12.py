"""Module 12: feat: add metrics collection."""

class Component12:
    """Implementation of component 12."""

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
        return f"Component12(initialized={self._initialized})"
