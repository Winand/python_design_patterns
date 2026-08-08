# Command Pattern
**Command** is a behavioral pattern in which a request object encapsulates
all the information needed to perform a specific action. This allows you to
parametrize objects with actions, queue/delay actions, perform
undo/redo and log/replay logic. It is widely used in non-destructive editors
for undo/redo, transaction systems, task queues, macro recording, etc.

## Real life examples
- Airflow tasks (operators) are command objects executed using `execute()` method
- GUI button `onClick` method is parametrized with a specific action
- Video editors apply effects/transformations as command objects, enabling non-destructive editing
