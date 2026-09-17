---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "67ff5591-f9f4-8007-829e-710ea22d5029"
created: 1744786834.192271
updated: 1744786868.154326
resource_section: true
---

# IndexError Duplicate Removal Fix

## User

a=\[1,1,1,2,2,3,3,3,3,4,4,5\]

count = 0
j=1
n=len(a)
for i in range(n):
    if a\[i\]==a\[i+1\]:
        continue 
    if a\[i\]!=a\[i+1\]:
        a\[j\] = a\[i+1\]
        j+=1
        count+=1
print (a\[:count\]) index error

## Assistant

You're encountering an **`IndexError`** because in the loop:

```python
for i in range(n):
 if a\[i\] == a\[i+1\]:
```

You're trying to access `a\[i+1\]`, which becomes out of bounds when `i` reaches the last index (`i = n-1`). At that point, `a\[i+1\]` is `a\[n\]`, which is **not defined**.

---

### **Corrected Version:**
If you're trying to **remove duplicates** from a sorted list `a` **in-place**, here's how to do it properly:

```python
a = \[1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5\]

n = len(a)
if n == 0:
 print(\[\])
else:
 j = 0 # points to the index of the last unique element
 for i in range(1, n):
 if a\[i\] != a\[j\]:
 j += 1
 a\[j\] = a\[i\]

 print(a\[:j+1\]) # unique elements
```

---

### **Explanation (as a student would write in an exam):**

> In the above code, we remove duplicates from a sorted array by maintaining a pointer `j` that keeps track of the position of the last unique element found. We iterate from the second element (index 1) to the end of the array, and whenever we find a new unique element, we increment `j` and replace `a\[j\]` with that unique value. At the end, we return the list from `a\[0\]` to `a\[j\]`, which contains all unique elements in order.

---

Let me know if you want a version that works for **unsorted** arrays as well.

## Resources

No structured attachments or external references were present in this conversation.
