# chain/support_handlers.py
from chain.base import Handler

class LowPriorityHandler(Handler):
    def _can_handle(self, request):
        return request.get("priority") == "low"

    def _process(self, request):
        print(f"Low priority ticket processed: {request['description']}")
        return "processed by low"

class MediumPriorityHandler(Handler):
    def _can_handle(self, request):
        return request.get("priority") == "medium"

    def _process(self, request):
        print(f"Medium priority ticket processed: {request['description']}")
        return "processed by medium"

class HighPriorityHandler(Handler):
    def _can_handle(self, request):
        return request.get("priority") == "high"

    def _process(self, request):
        print(f"High priority ticket processed: {request['description']}")
        return "processed by high"


