class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    contact_1 = ("Riley", "123-456-7890")
    print(contact_1)
    
class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value)
        self.key = key
        self.value = value
        self.next = None

        contact_1 = Contact("Riley", "123-456-7890")
        node_1 = Node(contact_1.name, contact_1)
        print(node_1.value)
        print(node_1.next)

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
        
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size


    def insert(self, key, value):
        index = self.hash_function(key)

        current = self.data[index]

        if self.data[index] is None:
          self.data[index] = Node(key,value)
          return

        while current:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break

            current = current.next

        current.next = Node(key,value)



    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key ==key:
                return current.value
            current = current.next

        return None
        
# Test your hash table implementation here.  
