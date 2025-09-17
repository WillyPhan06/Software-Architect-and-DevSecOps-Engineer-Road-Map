#Sample code for Abstract Factory pattern

# clouds.py
from __future__ import annotations
from abc import ABC, abstractmethod

# Product interfaces
class Compute(ABC):
    @abstractmethod
    def launch(self, name: str) -> str: ...

class SecretStore(ABC):
    @abstractmethod
    def put(self, key: str, value: str) -> None: ...
    @abstractmethod
    def get(self, key: str) -> str: ...

# Concrete products: AWS
class EC2(Compute):
    def launch(self, name: str) -> str: return f"EC2 instance {name} launched"

class SecretsManager(SecretStore):
    _secrets: dict[str, str] = {}
    def put(self, key: str, value: str) -> None: self._secrets[key] = value
    def get(self, key: str) -> str: return self._secrets[key]

# Concrete products: GCP
class GCE(Compute):
    def launch(self, name: str) -> str: return f"GCE VM {name} launched"

class SecretManager(SecretStore):
    _secrets: dict[str, str] = {}
    def put(self, key: str, value: str) -> None: self._secrets[key] = value
    def get(self, key: str) -> str: return self._secrets[key]

# Abstract Factory
class CloudFactory(ABC):
    @abstractmethod
    def compute(self) -> Compute: ...
    @abstractmethod
    def secrets(self) -> SecretStore: ...

# Concrete factories
class AWSFactory(CloudFactory):
    def compute(self) -> Compute: return EC2()
    def secrets(self) -> SecretStore: return SecretsManager()

class GCPFactory(CloudFactory):
    def compute(self) -> Compute: return GCE()
    def secrets(self) -> SecretStore: return SecretManager()

# Client code uses only the abstract factory & product interfaces
def bootstrap_app(factory: CloudFactory) -> None:
    c = factory.compute()
    s = factory.secrets()
    print(c.launch("app-vm"))
    s.put("DB_PASSWORD", "s3cr3t")
    print("secret:", s.get("DB_PASSWORD"))
