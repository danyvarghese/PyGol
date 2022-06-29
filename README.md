# PyGol
**PyGol** is novel Inductive Logic Programming(ILP) system based on **Meta Inverse Entailment(MIE)** using Python. MIE is similar to Mode-Directed Inverse Entailment (MDIE) but does not require mode declarations. MIE can be applied to tabular and relational datasets with minimal user intervention or parameter setting. In MIE, each hypothesis clause is derivable from a **meta theory** generated automatically from the background knowledge. Meta theory can also be viewed as a higher-order language bias that defines the hypothesis space. 

**PyGol** is provided as a Python library which can be used in Python programs (e.g. Jupyter notebooks). It can also connect with **SWI-Prolog** via **Pyswip**. 

**PyGol** is free to use for non-commercial research and education. If you use PyGol for research, please cite the paper : 
```cmdDany Varghese and  Alireza Tamaddoni-Nezhad, **Towards Automated Data Science using
Meta Inverse Entailment**,  In: Proceeding of ILP 2022 (to appear).
```
Anyone wishing to use PyGol for commercial purposes should contact either Dany Varghese(dany.varghese@surrey.ac.uk) or Alireza Tamaddoni-Nezhad(a.tamaddoni-nezhad@surrey.ac.uk).

## Contributions
* An ILP approach **Meta Inverse Entailment(MIE)**
* An algorithm to generate **Meta Clause Set(MCS) **
* Defining Most Speific Clause using MCS
* A new **higher-order** language bias **Meta Theory(MT)** - Automatically generating from MCS
* **Abductive Learning** using MIE
* Meta Inverse Entailment (MIE) for the purpose of **automated data science**

## Using PyGol
**PyGol** package is provided as a **C** code. The shared-object file **pygol.so** runs in Python. The current shared-object file is compiled for **Linux x86_64** systems.

For all other systems, you can find the **C** code in the folder **"Code"** and convert it to shared-object by executing the following commands;

```cmd
gcc <Python_Environment_Variable> -c -fPIC pygol.c -o pygol.o
gcc pygol.o -shared -o pygol.so
```
## Example Problem
PyGol requires four inputs, either in the form of files or a list
1. Background knowledge (BK)
2. Positive example
3. Negative example
4. Constants

The following code demonstrates learning the famous Michalski train problem. **Any file extensions can be used for the input files.**

### Background knowledge - `BK.pl`
```prolog
.
.
has_car(west10,car_101).
has_car(west10,car_102).
short(car_101).
long(car_102).
shape(car_101,u_shaped).
shape(car_102,rectangle).
open(car_101).
.
.
```
### Positive Example - `pos_example.f`
```prolog
eastbound(east1).
eastbound(east2).
eastbound(east3).
eastbound(east4).
eastbound(east5).
```
### Negative Example - `neg_example.n`
```prolog
eastbound(west6).
eastbound(west7).
eastbound(west8).
eastbound(west9).
eastbound(west10).
```
### Constants - `Python List`
```Python
const=["elipse", "hexagon","rectangle","u_shaped","triangle","hexagon","circle","nil"]
```
### Python Execution
```python
# Import package from root folder
import sys
sys.path.insert(0, '../../')
from pygol import *

#Define the constants
const=["elipse", "hexagon","rectangle","u_shaped","triangle","hexagon","circle","nil"]

#Generate the bottom clauses
P, N = bottom_clause_generation(constant_set = const,  container = "memory")

# Split examples into train and test subsets
Train_P, Test_P, Train_N, Test_N=pygol_train_test_split(test_size=0, positive_file_dictionary=P, 
                                                                 negative_file_dictionary=N)

#Learning Phase/Training Phase using Python
model= pygol_learn(Train_P, Train_N,  max_neg=0, max_literals=3, key_size=1,optimize=False)
```

### Output from Learning Phase
```
+----------+ Training +----------+
['eastbound(A):-has_car(A,B),closed(B),short(B)']
+---------------------+------------------+------------------+
|       n = 10        | Positive(Actual) | Negative(Actual) |
+=====================+==================+==================+
| Positive(Predicted) | 5                | 0                |
+---------------------+------------------+------------------+
| Negative(Predicted) | 0                | 5                |
+---------------------+------------------+------------------+
+-------------+---+
|   Metric    | # |
+=============+===+
| Accuracy    | 1 |
+-------------+---+
| Precision   | 1 |
+-------------+---+
| Sensitivity | 1 |
+-------------+---+
| Specificity | 1 |
+-------------+---+
| F1 Score    | 1 |
+-------------+---+
```
## Learning Settings
- ILP  Learning Approach :- **pygol_learn()**
- ILP Cross-Validation Approach :- **pygol_cross_validation()**
- Dealing with typical data science dataset :- **pygol_auto_learn()**
- Dealing with typical data science dataset(CV) :- **pygol_auto_cross_validation()**

For further information, please find the [manual](https://github.com/danyvarghese/PyGol/blob/debbe3024fda4cfaf33936e76dfd9455e455c39c/Manual_Pygol.pdf).

## Bug Reports and Feature Requests
Please submit all bug reports and feature requests as issues on this GitHub repository.
