# client.py
from chain.support_handlers import LowPriorityHandler, MediumPriorityHandler, HighPriorityHandler

def main():
    # Step 1: Create handlers
    low_handler = LowPriorityHandler()
    medium_handler = MediumPriorityHandler()
    high_handler = HighPriorityHandler()

    # Step 2: Build the chain: Low → Medium → High
    low_handler.set_successor(medium_handler)
    medium_handler.set_successor(high_handler)

    # Step 3: Example requests
    requests = [
        {"priority": "low", "description": "Reset user password"},
        {"priority": "medium", "description": "Install new software"},
        {"priority": "high", "description": "Server is down!"},
        {"priority": "urgent", "description": "Critical security breach"}  # no handler
    ]

    # Step 4: Send requests through the chain
    for req in requests:
        print(f"\nProcessing request: {req['description']}")
        result = low_handler.handle(req)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
