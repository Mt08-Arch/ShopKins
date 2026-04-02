from typing import Any, Callable, Dict, List

class EventBus:
    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, listener: Callable):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    async def emit(self, event_type: str, **kwargs: Any):
        if event_type in self._listeners:
            for listener in self._listeners[event_type]:
                await listener(**kwargs)

events = EventBus()
