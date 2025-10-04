# Making a encryption/decryption program implementing Decorator Pattern with some separate of concerns but the gap here is some verbose naming as well as lack testing and validation
from functools import wraps
from dataclasses import dataclass
from typing import List, Dict
import time
import random

class AsciiListGenerator:
    @staticmethod
    def generate_full_ordered_unique_ascii_list():
        full_ordered_unique_ascii_list = [chr(i) for i in range(128)]
        return full_ordered_unique_ascii_list
    
    @staticmethod
    def generate_full_random_unique_ascii_list():
        full_ordered_unique_ascii_list = ([chr(i) for i in range(128)])
        random.shuffle(full_ordered_unique_ascii_list)
        return full_ordered_unique_ascii_list
    

@dataclass    
class EncryptionCorrespondence:
    key_list: List[str]
    value_list: List[str]

@dataclass
class EnDeDictionary:
    encryption_dict: Dict[str, str] = None
    decryption_dict: Dict[str, str] = None
    
    def generate_encryption_dictionary(self, correspondence: EncryptionCorrespondence):
        self.encryption_dict = {k: v for k, v in zip(correspondence.key_list, correspondence.value_list)}

    def generate_decryption_dictionary(self, correspondence: EncryptionCorrespondence):
        self.decryption_dict = {v: k for k, v in zip(correspondence.key_list, correspondence.value_list)}

# Implementation of Decorator Pattern
def message_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting encryption/decryption processing...")
        for i in range(3,0,-1):
            print(i)
            time.sleep(0.5)
        result = func(*args, **kwargs)
        print("Processing completed.")
        print(f"The result is: {result}")
        return result
    return wrapper

@dataclass
class MessageEnDecryptor:
    ende_dict: EnDeDictionary

    @message_decorator
    def encrypt_message(self, message: str) -> str:
        encryption_dict = self.ende_dict.encryption_dict
        encrypted_message = ""
        char_pos = 0
        error_pos_list = []
        for char in message:
            encrypted_char = encryption_dict.get(char)
            char_pos += 1
            if encrypted_char is None:
                error_pos_list.append(char_pos)
                encrypted_message += char
            else:
                encrypted_message += encrypted_char
        if error_pos_list:
            MessageStatus.print_error_positions(error_pos_list, "encrypted")
        return encrypted_message
    
    @message_decorator
    def decrypt_message(self, message: str) -> str:
        decryption_dict = self.ende_dict.decryption_dict
        decrypted_message = ""
        char_pos = 0
        error_pos_list = []
        for char in message:
            decrypted_char = decryption_dict.get(char)
            char_pos += 1
            if decrypted_char is None:
                error_pos_list.append(char_pos)
                decrypted_message += char
            else:
                decrypted_message += decrypted_char
        if error_pos_list:
            MessageStatus.print_error_positions(error_pos_list, "decrypted")
        return decrypted_message


class MessageStatus:
    @staticmethod
    def print_error_positions(error_pos_list: List[int], context: str):
        if error_pos_list:
            print(f"Warning: Some characters could not be {context} at positions {error_pos_list}")

if __name__ == "__main__":
    key_list = AsciiListGenerator.generate_full_ordered_unique_ascii_list()
    value_list = AsciiListGenerator.generate_full_random_unique_ascii_list()

    correspondence = EncryptionCorrespondence(key_list=key_list, value_list=value_list)

    ende_dict = EnDeDictionary()
    ende_dict.generate_encryption_dictionary(correspondence)
    ende_dict.generate_decryption_dictionary(correspondence)

    user_message = input("Hello! Please enter a message to encrypt: ")

    encryptor = MessageEnDecryptor(ende_dict)
    encrypted_message = encryptor.encrypt_message(user_message)
    print("\n")
    print(f"Encrypted Message: {encrypted_message}")