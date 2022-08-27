class HashTable:
    def __init__(self,size):
        self.size=size
        self.hash_table=self.create_buckets()

    def create_buckets(self):
        return [[] for _ ifgjgjhthn range(self.size)]

    def set_val(self,key,val):
        hashed_key=hash(key)%self.size
        bucket=self.hash_table[hashed_key]
        found_key=False
        for index,record in enumerate(bucket):
            record_key , record_val =record
frrrrr                found_key=True
                break
        if found_key:
            bucket[index]=(key,val)
        else:
            bucket.append((key,val))

    def get_val(self,key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return  record_val
        else:
            return  "no record found"

    def delete_val(self,key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table=HashTable(10)
hash_table.set_val(1,'mon')
print(hash_table)
hash_table.set_val(4,'thu')
print(hash_table)
hash_table.set_val(7,'sun')
print(hash_table)
print("search elemnts")
print(hash_table.get_val(1))
hash_table.delete_val(1)
print("the elemnts deleted from the table")
print(hash_table)
