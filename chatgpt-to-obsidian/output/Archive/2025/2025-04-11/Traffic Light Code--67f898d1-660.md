---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "67f898d1-6600-8007-ac4b-3469699acc61"
created: 1744345297.917504
updated: 1744345304.866636
resource_section: true
---

# Traffic Light Code

## User

light one int 
red1 = 10;

int yellow1 = 9; 

int green1 = 8;

// light two int 

red2 = 13;

int yellow2 = 12; 

int green2 = 11; 

void setup(){

// light one 

pinMode(red1, OUTPUT);

pinMode(yellow1, 

OUTPUT); pinMode(green1, complete this code

## Assistant

Certainly. Here's the completed and corrected version of your Arduino traffic light control code for two sets of traffic lights:

```cpp
// Light one pins
int red1 = 10;
int yellow1 = 9;
int green1 = 8;

// Light two pins
int red2 = 13;
int yellow2 = 12;
int green2 = 11;

void setup() {
 // Light one pin modes
 pinMode(red1, OUTPUT);
 pinMode(yellow1, OUTPUT);
 pinMode(green1, OUTPUT);

 // Light two pin modes
 pinMode(red2, OUTPUT);
 pinMode(yellow2, OUTPUT);
 pinMode(green2, OUTPUT);
}

void loop() {
 // Light one: Green, Light two: Red
 digitalWrite(green1, HIGH);
 digitalWrite(red2, HIGH);
 delay(5000);

 // Light one: Yellow
 digitalWrite(green1, LOW);
 digitalWrite(yellow1, HIGH);
 delay(2000);

 // All lights off briefly
 digitalWrite(yellow1, LOW);
 digitalWrite(red2, LOW);
 delay(1000);

 // Light one: Red, Light two: Green
 digitalWrite(red1, HIGH);
 digitalWrite(green2, HIGH);
 delay(5000);

 // Light two: Yellow
 digitalWrite(green2, LOW);
 digitalWrite(yellow2, HIGH);
 delay(2000);

 // All lights off briefly
 digitalWrite(yellow2, LOW);
 digitalWrite(red1, LOW);
 delay(1000);
}
```

**Explanation:** 
This code simulates a simple two-way traffic light system. Each light cycles through green, yellow, and red in a coordinated fashion to ensure proper traffic flow. The delays can be adjusted based on required timing.

Let me know if you'd like to integrate buttons, sensors, or simulate pedestrian crossings as well.

## Resources

No structured attachments or external references were present in this conversation.
