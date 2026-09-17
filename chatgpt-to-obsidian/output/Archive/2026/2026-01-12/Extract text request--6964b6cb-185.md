---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6964b6cb-185c-8322-8818-db97382d85b2"
created: 1768208091.761923
updated: 1768208120.49471
resource_section: true
---

# Extract text request

## User

Extract text

## Assistant

Below is the **extracted and cleaned text** from the image (code + plot labels), reconstructed accurately from the visible content:

---

### Python Code (Leaky ReLU Plot)

```python
import matplotlib.pyplot as plt
import numpy as np

def leaky_relu(x, alpha=0.01):
 return np.maximum(alpha * x, x)

x = np.linspace(-10, 10, 100)
y = leaky_relu(x)

plt.plot(x, y)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Leaky ReLU Activation Function")
plt.grid()
plt.show()
```

---

### Plot Title

**Leaky ReLU Activation Function**

### Axis Labels

- X-axis: **Input**
- Y-axis: **Output**

---

### Interpretation (student-style explanation)

The given code implements and visualizes the **Leaky ReLU activation function**. For positive input values, the function behaves linearly. For negative values, instead of becoming zero, it allows a small slope controlled by the parameter α (alpha). This helps in overcoming the dying ReLU problem and ensures gradient flow during backpropagation.

---

If you want, I can now:

- Write a 5-mark or 10-mark exam answer on Leaky ReLU 
- Compare ReLU vs Leaky ReLU 
- Explain mathematically with formula and graph description 
- Convert this into project or lab record format

## Resources

### Local attachments
- [1000045557.jpg](../../../Raw/Export/file_000000009f387206a641880cfb3c9f67.dat)
