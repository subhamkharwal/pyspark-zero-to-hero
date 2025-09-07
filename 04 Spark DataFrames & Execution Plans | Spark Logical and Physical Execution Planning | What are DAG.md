# Spark DataFrames and Execution Planning

## DataFrames Overview
DataFrames are structured APIs built on top of RDDs (Resilient Distributed Datasets). They provide a table-like structure with:
- Rows and columns organization
- Schema definition with column metadata
- Partitioned data storage
- Immutable nature

### Immutability Example
```
Original DataFrame
    → Filter(salary > 10000) → New DataFrame 1
        → Select(name, departmentId, salary) → New DataFrame 2
```

Key point: Instead of modifying existing DataFrames, transformations create new ones.

## Parallel Processing with DataFrames
- Data is stored in partitions
- Each partition can be processed independently
- Multiple cores can work on different partitions simultaneously
- Example: 4 partitions = 4 parallel tasks

![image](https://github.com/user-attachments/assets/3e464d5d-77a5-41d4-bc4f-e918875c5161)


## Execution Planning Process

### 1. Logical Planning Phase
1. User submits code
2. Creation of unresolved logical plan
3. Validation against catalog (table/column names)
4. Generation of resolved logical plan
5. Optimization by Catalyst Optimizer
6. Production of optimized logical plan

![image](https://github.com/user-attachments/assets/f5b1119e-ed46-4f28-b553-689cf96cd212)


### 2. Physical Planning Phase
1. Generation of multiple physical plans
2. Cost evaluation for each plan
3. Selection of most efficient plan
4. Execution on cluster

![image](https://github.com/user-attachments/assets/2de19ffe-54e3-4de1-858a-6c3262834a1c)


## DAG (Directed Acyclic Graph)
- Represents the execution flow
- Shows dependencies between operations
- Used by Spark to manage execution

graph TD
    A[User Code] --> B[Unresolved Logical Plan]
    B --> C[Catalog Validation]
    C --> D[Resolved Logical Plan]
    D --> E[Catalyst Optimizer]
    E --> F[Optimized Logical Plan]
    F --> G[Multiple Physical Plans]
    G --> H[Cost Model Evaluation]
    H --> I[Best Physical Plan Selection]
    I --> J[Cluster Execution]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#bbf,stroke:#333,stroke-width:2px
    style J fill:#bfb,stroke:#333,stroke-width:2px
