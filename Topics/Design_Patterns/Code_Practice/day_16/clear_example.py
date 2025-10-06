# Flyweight class
class Character:
    def __init__(self, char):
        self.char = char  # Intrinsic state (shared)
        self.font = "Arial"
        self.size = 12

    def display(self, position):
        # Extrinsic state (not shared)
        print(f"Character: {self.char}, Font: {self.font}, Size: {self.size}, Position: {position}")


# Flyweight Factory
class CharacterFactory:
    def __init__(self):
        self._characters = {}

    def get_character(self, char):
        if char not in self._characters:
            self._characters[char] = Character(char)
        return self._characters[char]


# Client code
factory = CharacterFactory()

# Create many characters, but reuse existing ones
chars = "nani kore baba cha cha haha war war"
positions = [(i, 0) for i in range(len(chars))]

for char, pos in zip(chars, positions):
    character_obj = factory.get_character(char)
    character_obj.display(pos)

# Output shows characters reusing the same objects
