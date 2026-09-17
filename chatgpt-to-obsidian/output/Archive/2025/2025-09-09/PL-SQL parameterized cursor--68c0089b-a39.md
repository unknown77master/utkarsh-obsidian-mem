---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "68c0089b-a398-8322-bdf5-d35da40720df"
created: 1757415788.612619
updated: 1757415824.474298
resource_section: true
---

# PL/SQL parameterized cursor

## User

6. Cursors: (All types: Implicit, Explicit, Cursor FOR Loop, Parameterized Cursor)

Write a PL/SQL block of code using parameterized Cursor that will merge the data available in the newly created table N_Roll_Call with the data available in the table O_Roll_Call. If the data in the first table already exists in the second table then that data should be skipped.

Note: Instructor will frame the problem statement for writing PL/SQL block using all types of Cursors in line with above statement.

Write this for practical with Title, problem statement,theory

## Assistant

Here’s a structured practical write-up for your lab record with **Title, Problem Statement, Theory, and PL/SQL code** for **Parameterized Cursor**. I’ve written it in a formal academic tone, like how you would submit in practical files. 

---

# **Title** 
Implementation of Parameterized Cursor in PL/SQL to Merge Data Between Tables 

---

# **Problem Statement** 
Write a PL/SQL block using a **Parameterized Cursor** that merges data from a newly created table **N_Roll_Call** into an existing table **O_Roll_Call**. If a record from **N_Roll_Call** already exists in **O_Roll_Call**, it should be skipped to avoid duplication. 

---

# **Theory** 
In PL/SQL, cursors are used to process multiple rows returned by a query, one at a time. There are different types of cursors: 

1. **Implicit Cursor**: Automatically created by Oracle when a DML statement (INSERT, UPDATE, DELETE) or a query (SELECT INTO) is executed. 
2. **Explicit Cursor**: Declared by the programmer to process query results row by row. 
3. **Cursor FOR Loop**: A loop structure that simplifies explicit cursor handling without requiring explicit OPEN, FETCH, and CLOSE statements. 
4. **Parameterized Cursor**: Allows passing parameters dynamically at runtime, making the cursor reusable for different input conditions. 

In this experiment, a **Parameterized Cursor** is used to compare roll numbers between the two tables. Only records that do not already exist in the old table (**O_Roll_Call**) will be inserted, ensuring data integrity and avoiding duplication. 

---

# **PL/SQL Program Using Parameterized Cursor**

```sql
DECLARE
 -- Parameterized Cursor: takes roll number as parameter
 CURSOR c_check_roll(p_roll N_Roll_Call.Roll_No%TYPE) IS
 SELECT Roll_No 
 FROM O_Roll_Call 
 WHERE Roll_No = p_roll;

 -- Variable to hold data from N_Roll_Call
 v_roll N_Roll_Call.Roll_No%TYPE;
 v_name N_Roll_Call.Student_Name%TYPE;

 -- Variable to check existence
 v_exist O_Roll_Call.Roll_No%TYPE;
BEGIN
 -- Iterate through all rows in N_Roll_Call
 FOR rec IN (SELECT Roll_No, Student_Name FROM N_Roll_Call) LOOP
 
 -- Check if record already exists using parameterized cursor
 OPEN c_check_roll(rec.Roll_No);
 FETCH c_check_roll INTO v_exist;

 -- If record not found, insert into O_Roll_Call
 IF c_check_roll%NOTFOUND THEN
 INSERT INTO O_Roll_Call(Roll_No, Student_Name)
 VALUES(rec.Roll_No, rec.Student_Name);
 DBMS_OUTPUT.PUT_LINE('Inserted Roll No: ' || rec.Roll_No);
 ELSE
 DBMS_OUTPUT.PUT_LINE('Skipped Roll No: ' || rec.Roll_No || ' (Already Exists)');
 END IF;

 CLOSE c_check_roll;
 END LOOP;
END;
/
```

---

# **Explanation of Code** 
- A **Parameterized Cursor** `c_check_roll(p_roll)` is declared to check whether a given roll number exists in the old table. 
- A `FOR LOOP` fetches each student record from the **N_Roll_Call** table. 
- For each record, the parameterized cursor is opened with the roll number. 
- If the roll number does not exist in **O_Roll_Call**, the record is inserted. Otherwise, it is skipped. 
- The output is displayed using `DBMS_OUTPUT.PUT_LINE`. 

---

# **Output (Sample)** 

If **N_Roll_Call** contains: 
```
Roll_No | Student_Name
--------|--------------
101 | Rahul
102 | Sneha
103 | Amit
```

And **O_Roll_Call** already contains: 
```
Roll_No | Student_Name
--------|--------------
101 | Rahul
```

**After execution**, the output will be: 
```
Skipped Roll No: 101 (Already Exists)
Inserted Roll No: 102
Inserted Roll No: 103
```

And **O_Roll_Call** will now contain: 
```
Roll_No | Student_Name
--------|--------------
101 | Rahul
102 | Sneha
103 | Amit
```

---

Would you like me to also **draft the PL/SQL programs for Implicit, Explicit, and Cursor FOR Loop** (so your practical file has all four cursor types in continuation with this one)?

## Resources

No structured attachments or external references were present in this conversation.
