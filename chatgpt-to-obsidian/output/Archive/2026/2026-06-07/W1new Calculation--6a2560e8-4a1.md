---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a2560e8-4a14-8324-9540-1af112d68522"
created: 1780834576.820404
updated: 1780834774.930382
resource_section: true
---

# W1new Calculation

## User

solve for w1new
w1new = w1old - a(X - w1old) 
where: w1old = \[0,0,1,1\] X = \[0,0,0,1\] a = 0.5

## Assistant

Given:

\\[
W_{1(new)} = W_{1(old)} - a(X - W_{1(old)})
\\]

Where:

\\[
W_{1(old)} = \[0,0,1,1\]
\\]

\\[
X = \[0,0,0,1\]
\\]

\\[
a = 0.5
\\]

### Step 1: Calculate \((X - W_{1(old)})\)

\\[
\[0,0,0,1\] - \[0,0,1,1\]
\\]

\\[
= \[0-0,\;0-0,\;0-1,\;1-1\]
\\]

\\[
= \[0,0,-1,0\]
\\]

### Step 2: Multiply by learning rate \(a=0.5\)

\\[
0.5\[0,0,-1,0\]
\\]

\\[
= \[0,0,-0.5,0\]
\\]

### Step 3: Update the weight vector

\\[
W_{1(new)} = \[0,0,1,1\] - \[0,0,-0.5,0\]
\\]

\\[
= \[0-0,\;0-0,\;1-(-0.5),\;1-0\]
\\]

\\[
= \[0,0,1.5,1\]
\\]

### Final Answer

\\[
\boxed{W_{1(new)} = \[0,\;0,\;1.5,\;1\]}
\\]

## User

thanks got it

## Assistant

You're welcome!

A quick shortcut for these updates:

\\[
W_{new}=W_{old}-a(X-W_{old})
\\]

can be rewritten as

\\[
W_{new}=(1+a)W_{old}-aX
\\]

For your values:

\\[
W_{new}=1.5\[0,0,1,1\]-0.5\[0,0,0,1\]
\\]

\\[
=\[0,0,1.5,1.5\]-\[0,0,0,0.5\]
\\]

\\[
=\[0,0,1.5,1\]
\\]

This form is often useful in ANN numerical problems because it reduces the number of intermediate calculations.

Glad it clicked. Feel free to send the next numerical if you're practicing for exams.

## User

sure

## Assistant

Great. For ANN numerical questions, a good exam approach is:

1. **Write the formula first** (1 mark is often awarded just for this).
2. **Substitute the given values clearly.**
3. **Show intermediate calculations in vector/matrix form.**
4. **Box the final answer.**

For competitive learning rules, Hebbian learning, Perceptron learning, Delta rule, Backpropagation, Kohonen SOM, Hamming Network, and Hopfield Network numericals, try to keep calculations organized in a table. Examiners usually prefer neat steps over compressed calculations.

If you get stuck on any ANN numerical, send the question exactly as it appears (photo or text), and I'll solve it in exam-writing format.

## Resources

No structured attachments or external references were present in this conversation.
