# Core Apache Spark Concepts

## 1. Partitions
Partitions are chunks of data that enable parallel processing in Spark.

### Key Points:
- Input data is broken down into smaller chunks called partitions
- Each partition can be processed independently
- Enables parallel processing across executors
- Example: Like dividing a bag of marbles into separate pouches
- Four partitions can be processed by four tasks simultaneously

## 2. Transformations
Transformations are instructions that modify or transform data.

### Types of Transformations:
1. **Narrow Transformations**
   - Each input partition contributes to at most one output partition
   - Example operations: `filter`, `select`, `map`
   - No data shuffling required between partitions

2. **Wide Transformations**
   - Input partitions may contribute to multiple output partitions
   - Requires data shuffling between partitions
   - Example operations: `groupBy`, `join`, `repartition`
   - Results in shuffle operations
  
![image](https://github.com/user-attachments/assets/190aa623-6321-48d9-85d7-1892b00d48fc)


### Example Transformation Chain:
```sql
-- Starting with employee dataset
.filter(salary > 10000)           -- Transformation 1
.select(name, departmentId, salary) -- Transformation 2
.groupBy(departmentId)             -- Transformation 3
```

## 3. Actions
Actions trigger the actual execution of transformations.

### Types of Actions:
1. **View Data in Console**
   - Examples: `show()`, `take()`
2. **Collect Data in Native Language**
   - Example: `collect()`
3. **Write to Output Sources**
   - Example: `write.parquet()`

## 4. Lazy Evaluation
Spark uses lazy evaluation to optimize resource usage and performance.

### Benefits:
- Allows Spark to optimize the execution plan
- Reduces unnecessary computations
- Better resource planning

### Sandwich Shop Analogy:
1. **Eager Evaluation (Poor)**
   - Start making sandwich immediately
   - Customer changes order
   - Result: Wasted time and resources

2. **Lazy Evaluation (Better)**
   - Wait for complete order and payment (action)
   - Plan resources efficiently
   - Execute optimized plan
   - Result: Efficient resource usage

## 5. Spark Session
The entry point for Spark applications.

### Characteristics:
- Represents the driver process
- One Spark application = One Spark session
- Responsible for:
  - Executing code in cluster
  - Managing resources
  - Coordinating execution

### Key Points:
- Acts as the main interface for Spark functionality
- Creates and manages SparkContext
- Provides unified access to various Spark features
