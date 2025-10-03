# pipeline/base.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, final
import logging
import time

log = logging.getLogger(__name__)

class DataPipeline(ABC):
    """Template Method: run() is the skeleton — subclasses implement steps."""

    @final
    def run(self, source: Any) -> Any:
        """Template method — do not override in subclasses."""
        start = time.perf_counter()
        self._before_run(source)
        raw = self.extract(source)
        data = self.transform(raw)
        self.validate(data)
        result = self.load(data)
        self._after_run(result, time.perf_counter() - start)
        return result

    def _before_run(self, source: Any) -> None:
        log.debug("Starting pipeline for %s", source)

    def _after_run(self, result: Any, elapsed: float) -> None:
        log.debug("Finished pipeline in %.3fs, result=%s", elapsed, result)

    @abstractmethod
    def extract(self, source: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def transform(self, raw: Any) -> Any:
        raise NotImplementedError

    def validate(self, data: Any) -> None:
        """Optional hook (default: no-op). Subclasses can override to raise on bad data."""
        return None

    @abstractmethod
    def load(self, data: Any) -> Any:
        raise NotImplementedError

