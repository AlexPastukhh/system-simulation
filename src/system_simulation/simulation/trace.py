from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class Change:
    path: str
    before: Any
    after: Any


@dataclass(frozen=True)
class TraceFrame:
    step: int
    event: str
    description: str
    changes: tuple[Change, ...]
    snapshot: dict[str, Any]


class SimulationTrace:
    def __init__(self) -> None:
        self._frames: list[TraceFrame] = []

    @property
    def frames(self) -> tuple[TraceFrame, ...]:
        return tuple(self._frames)

    def record(self, *, event: str, description: str, changes: list[Change], snapshot: dict[str, Any]) -> TraceFrame:
        frame = TraceFrame(len(self._frames), event, description, tuple(changes), snapshot)
        self._frames.append(frame)
        return frame

    def as_dicts(self) -> list[dict[str, Any]]:
        return [asdict(frame) for frame in self._frames]
