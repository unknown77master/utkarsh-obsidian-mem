---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "66e9ab08-777c-8007-ada9-f5d7c8961dd9"
created: 1726589704.679334
updated: 1726590828.138311
resource_section: true
---

# Unordered_map Methods Overview

## User

Explain all methods used in unordered_map in c++

## Assistant

In C++, the `unordered_map` is a container that stores elements formed by a combination of key-value pairs. It is implemented using a hash table, which allows for fast access to elements with constant average time complexity for search, insert, and delete operations. The keys in `unordered_map` are unique, and the order of elements is not maintained, as it is in a regular `map`. 

Here’s an overview of the commonly used methods of the `unordered_map` class:

### 1. **Element Access Methods**

- **`at(const key_type& key)`**: 
 - Returns a reference to the value that is mapped to the specified key. Throws an exception (`std::out_of_range`) if the key is not found.
 - **Example**:
 ```cpp
 unordered_map<int, string> umap;
 umap\[1\] = "one";
 cout << umap.at(1); // Output: one
 ```

- **`operator\[\](const key_type& key)`**:
 - If the key exists, it returns a reference to the value associated with the key. If the key does not exist, it inserts a new element with the given key and a default-constructed value.
 - **Example**:
 ```cpp
 unordered_map<int, string> umap;
 cout << umap\[1\]; // Inserts {1, ""} and outputs an empty string
 ```

### 2. **Iterators**

- **`begin()`** and **`end()`**:
 - Return an iterator to the first element and an iterator to the past-the-end element of the unordered map, respectively.
 - **Example**:
 ```cpp
 for (auto it = umap.begin(); it != umap.end(); ++it) {
 cout << it->first << ": " << it->second << endl;
 }
 ```

- **`cbegin()`**, **`cend()`**:
 - Return constant iterators to the beginning and end of the unordered map.

### 3. **Capacity**

- **`empty()`**:
 - Returns `true` if the unordered map is empty, otherwise `false`.
 - **Example**:
 ```cpp
 if (umap.empty()) {
 cout << "Map is empty!";
 }
 ```

- **`size()`**:
 - Returns the number of elements in the unordered map.
 - **Example**:
 ```cpp
 cout << "Size: " << umap.size();
 ```

- **`max_size()`**:
 - Returns the maximum number of elements that the unordered map can hold (based on system or implementation limitations).

### 4. **Modifiers**

- **`insert(const value_type& val)`**:
 - Inserts an element in the unordered map. If the key already exists, the element is not inserted.
 - **Example**:
 ```cpp
 umap.insert({2, "two"});
 ```

- **`insert_or_assign(const key_type& key, const mapped_type& obj)`**:
 - Inserts a new element if the key does not exist, or assigns the value to the key if it already exists.
 - **Example**:
 ```cpp
 umap.insert_or_assign(1, "new_one");
 ```

- **`erase(const key_type& key)`**:
 - Removes the element with the specified key.
 - **Example**:
 ```cpp
 umap.erase(1);
 ```

- **`erase(iterator position)`**:
 - Removes the element at the specified iterator position.

- **`clear()`**:
 - Removes all elements from the unordered map, making it empty.
 - **Example**:
 ```cpp
 umap.clear();
 ```

- **`emplace(Args&&... args)`**:
 - Constructs and inserts an element into the map in place.
 - **Example**:
 ```cpp
 umap.emplace(3, "three");
 ```

- **`emplace_hint(const_iterator hint, Args&&... args)`**:
 - Similar to `emplace()`, but uses a hint for the insertion position.

- **`swap(unordered_map& other)`**:
 - Exchanges the content of this map with another unordered map.

### 5. **Lookup**

- **`find(const key_type& key)`**:
 - Returns an iterator to the element with the specified key, or `end()` if the key is not found.
 - **Example**:
 ```cpp
 auto it = umap.find(1);
 if (it != umap.end()) {
 cout << "Found: " << it->second;
 }
 ```

- **`count(const key_type& key)`**:
 - Returns the number of elements with the specified key (0 or 1 for an unordered_map, since keys are unique).
 - **Example**:
 ```cpp
 cout << umap.count(1); // Outputs 1 if key 1 exists, else 0
 ```

- **`equal_range(const key_type& key)`**:
 - Returns a pair of iterators: the first points to the first element matching the key, and the second points to the element after the last match (or end).
 
### 6. **Bucket Interface**

- **`bucket_count()`**:
 - Returns the number of buckets in the unordered map.

- **`max_bucket_count()`**:
 - Returns the maximum number of buckets that the map can have.

- **`bucket_size(size_type n)`**:
 - Returns the number of elements in the bucket `n`.

- **`bucket(const key_type& key)`**:
 - Returns the bucket number where the element with the specified key is located.

### 7. **Hash Policy**

- **`load_factor()`**:
 - Returns the load factor, which is the ratio of the number of elements to the number of buckets.

- **`max_load_factor(float z)`**:
 - Sets the maximum load factor. If the load factor exceeds this value, the container automatically increases the number of buckets.

- **`rehash(size_type n)`**:
 - Rehashes the container so that it has at least `n` buckets.

- **`reserve(size_type n)`**:
 - Reserves at least enough space to accommodate `n` elements without rehashing.

### 8. **Observers**

- **`hash_function()`**:
 - Returns the hash function used by the unordered map.

- **`key_eq()`**:
 - Returns the function that compares keys for equality.

---

These are the most commonly used methods in `unordered_map`. They enable efficient manipulation of elements in a hash table while abstracting away the complexities of the underlying data structure.

## Resources

No structured attachments or external references were present in this conversation.
