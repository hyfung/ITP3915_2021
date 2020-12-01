# ITP3915_2021
Finished this programming assignment just for fun

## Requirement and Description
//TODO

## Solution Design Explained
* Main loop to receive user input
* Two states: Choice is '' or Choice is valid user input
  * Adding to current order
    * Parsing input to (COFFEE, QUANTITY, LARGE, COLD)
    * Append to current_list
    * Compute price
  * finishing current order and print summary
* Global state to store sales data


## Milestones
//TODO

## Running The Program
```bash
python3 asgn1.py
```

## Unittesting
Test case wrote against `compute_sales()` only
```bash
python3  Test_asgn1.py 
```

## Test Cases
|Input|Descriptions|Expected Output|
|-|-|-|
|1,2,Y,N||||
