# Vending Machine Design - Task 02.4.C

## 1. Understand & Rules
- **Products:** tea (15), coffee (25), juice (30)
- **Coins Accepted:** 5, 10, 20
- **Features:** Insert coins one by one, handle `cancel` at any time, return change using greedy coin distribution.

## 2. Flowchart (Mermaid)
```mermaid
graph TD
A[Start] --> B[Select Drink & Check Price]
B --> C{User enters coin or cancel?}
C -- "cancel" --> D[Refund full amount & Exit]
C -- "Invalid coin (not 5,10,20)" --> E[Reject coin & ask again]
C -- "Valid coin" --> F[Add to inserted total]
F --> G{Total >= Price?}
G -- No --> C
G -- Yes --> H[Calculate change and optimal coins]
H --> I[Dispense drink and change]
I --> J[End]
