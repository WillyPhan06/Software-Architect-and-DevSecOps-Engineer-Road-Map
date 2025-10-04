from chain.support_handlers import LowPriorityHandler, MediumPriorityHandler, HighPriorityHandler

def test_chain_routing():
    low = LowPriorityHandler()
    med = MediumPriorityHandler()
    high = HighPriorityHandler()
    low.set_successor(med)
    med.set_successor(high)

    tickets = [
        {"priority": "low", "description": "Fix typo"},
        {"priority": "medium", "description": "Update database"},
        {"priority": "high", "description": "Server down"},
        {"priority": "unknown", "description": "Unknown request"},
    ]

    results = [low.handle(t) for t in tickets]
    assert results == [
        "processed by low",
        "processed by medium",
        "processed by high",
        None,
    ]
