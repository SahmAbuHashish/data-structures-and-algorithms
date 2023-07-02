class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Generate a hash value for the given key
        return hash(key) % self.size

    def set(self, key, value):
        # Set the key and value pair in the table
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        # Check if the key already exists in the table
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                # Replace the existing value
                bucket[i] = (key, value)
                return

        # Key doesn't exist, add a new key-value pair
        bucket.append((key, value))

    def get(self, key):
        # Get the value associated with the given key in the table
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        # Search for the key in the bucket
        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value

        # Key not found
        return None

    def has(self, key):
        # Check if the key exists in the table
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        # Search for the key in the bucket
        for existing_key, _ in bucket:
            if existing_key == key:
                return True

        # Key not found
        return False

    def keys(self):
        # Get a collection of keys in the table
        keys = []
        for bucket in self.table:
            for key, _ in bucket:
                keys.append(key)
        return keys

    def hash(self, key):
        # Get the index in the collection for the given key
        return self._hash(key)
