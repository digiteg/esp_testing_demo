# **ESP8266 Simple Testing with examples in Micropython**

I was digging on internet for some examples about testing on ESP8266 in Micropython just for myself education purpose and I didn't find too much useful examples for me. So I decided to fill this gap and I hope this can be  also useful for others who are willing to deal with the topic or teach their students about basics and how to automate testing. Why ESP8266 ? Because it is cost-effective and highly integrated Wi-Fi MCU for IoT / smart things... applications


![Testing Phase](/img/introtesting.png)

## **Back to Testing..**

You can find lot of great articles about this topic explaining why it is worth spend so much time with Testing or why TDD make sense and so on. Usually my first and simple answer why is ist just because we want to suppress future costs of fixing bugs in production. Real nightmare of each developer doing coding for living should be spending hours of life time in finding bugs in code done by someone else running production with help of neurotic manager who is keeping him or her in pace..  
 
Some summary from my small internet research is bellow and it is about what could be considered and make sense in our case if we develop IoT application with ESP8266 and Micropython

### **Best practices for effective IoT Testing**

- Gray Box testing as it allows to design effective test case
- Gray Box allows you to know the OS, the architecture, third-party hardware, new connectivity and hardware device limitation.
- Real Time Operating System
- IoT Testing should be automated


### **Challenges of IOT Testing**
- Network and internal communication
- Security
- The system complexity & bugs present in the IOT technology
- Limitations in memory, processing power, bandwidth, battery life, etc.

<br/>
# Things used in this project

### **Hardware components**

 Things used in this project

### **Hardware components**

||Name|Qt||
| :---|:------------------------:|:---| ----:|
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |

### **Software apps and online services**
||Name|Qt||
| :---|:------------------------:|:---| ----:|
| Img | Raspberry Pi 3 Model B	 | ×1 | link |

### **Hand tools and fabrication machines**
||Name|Qt||
| :---|:------------------------:|:---| ----:|
| Img | Raspberry Pi 3 Model B	 | ×1 | link |

<br/>

# Long story short

Why Did We Build This?
Idea 💡
Hardware Build


![Types of Testing ](/img/typestesting.png)



## **Getting Started with first level - Unit Tests are just functions**


- Unit tests are typically made of three pieces, some setup, a number of assertions, and some tear-down. 

- Setup can be as simple as initializing the input values or as complex as creating and initializing concrete instances of a class. 

- Ultimately, the test occurs when an assertion is made, comparing the observed and expected values. For example, let us test  that our mean function successfully calculates the known value for a simple list.


**MicroPython assert Keyword**


    x = "hello Micropython"
    
    #if condition returns True, then nothing happens:
    assert x == "hello Micropython"
    
    #if condition returns False, AssertionError is raised:
    assert x == "bye"



#### Key features



#### Control - Arduino Shield




**Used I/Os of Arduino**




#### Installation of arm - video tutorial


## **Step 2: ..**
## **Step 3: ..**
## **Step 4: Testing the Model**

# Schematics

# Code

# Next steps

# Credits

## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```