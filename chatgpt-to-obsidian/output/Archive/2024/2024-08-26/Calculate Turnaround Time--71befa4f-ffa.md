---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "71befa4f-ffa7-4d1e-a1cc-ab95b59ca52d"
created: 1724666797.78762
updated: 1724666818.930832
resource_section: true
---

# Calculate Turnaround Time

## User

Write a python function to calculate Turn around time of process

## Assistant

Sure! The Turnaround Time (TAT) for a process is the total time taken between the submission of a process and its completion. It can be calculated using the formula:

\\[ \text{Turnaround Time} = \text{Completion Time} - \text{Arrival Time} \\]

Here is a Python function that calculates the Turnaround Time for a list of processes:

```python
def calculate_turnaround_time(processes):
 """
 Calculates the Turnaround Time for each process.
 
 Parameters:
 processes (list of dicts): A list where each process is represented by a dictionary with 'arrival_time' and 'completion_time'.
 
 Returns:
 list: A list of turnaround times for each process.
 """
 turnaround_times = \[\]
 
 for process in processes:
 tat = process\['completion_time'\] - process\['arrival_time'\]
 turnaround_times.append(tat)
 
 return turnaround_times

# Example usage:
processes = \[
 {'arrival_time': 0, 'completion_time': 10},
 {'arrival_time': 2, 'completion_time': 5},
 {'arrival_time': 4, 'completion_time': 9}
\]

tat = calculate_turnaround_time(processes)
print("Turnaround Times:", tat)
```

### Explanation:
- `processes`: This is a list of dictionaries where each dictionary represents a process with its `arrival_time` and `completion_time`.
- The function iterates through each process, calculates the turnaround time, and appends it to the `turnaround_times` list.
- Finally, the function returns the list of calculated Turnaround Times.

### Example Output:
For the `processes` given in the example, the output will be:
```python
Turnaround Times: \[10, 3, 5\]
```

You can modify the `processes` list with actual values based on your data.

## Resources

No structured attachments or external references were present in this conversation.
