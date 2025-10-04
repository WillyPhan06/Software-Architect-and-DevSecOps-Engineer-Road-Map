from dataclasses import dataclass
from copy import copy, deepcopy
from typing import List, Dict, Any

@dataclass
class NPC:
    name: str
    attributes: Dict[str, Any]
    position: List[float]


class NPCRegistry:
    _registry: Dict[str, NPC] = {}

    @classmethod
    def register_npc(cls, npc: NPC):
        cls._registry[npc.name] = npc

class NPCCloner: 
    @staticmethod
    def clone_npc(name: str, **overrides) -> NPC:
        org_npc = NPCRegistry._registry.get(name)
        if not org_npc:
            raise ValueError(f"NPC with name {name} not found in registry.")
        cloned_npc = deepcopy(org_npc)
        for key, value in overrides.items():
            setattr(cloned_npc, key, value)
        return cloned_npc
    
    
if __name__ == "__main__":
    org_npc = NPC(
        name="Goblin",
        attributes={"strength": 5, "agility": 7},
        position=[0.0, 0.0, 0.0]
        )
    NPCRegistry.register_npc(org_npc)
    deep_copied_npc_1 = NPCCloner.clone_npc("Goblin")
    modified_npc_1 = NPCCloner.clone_npc("Goblin", attributes={"strength": 10, "agility": 9})
    # non_existent_npc = NPCCloner.deep_clone_npc("Orc", "Orc_Clone1")
    print("Original NPC:", org_npc)
    print("Deep Copied NPC 1:", deep_copied_npc_1)
    print("Modified NPC 1:", modified_npc_1)


    
