# PyGol
**PyGol** is a novel Inductive Logic Programming(ILP) system based on **Meta Inverse Entailment(MIE)** using Python. MIE is similar to Mode-Directed Inverse Entailment (MDIE) but does not require mode declarations. MIE can be applied to tabular and relational datasets with minimal user intervention or parameter settings. In MIE, each hypothesis clause is derived from a **meta theory** generated automatically from background knowledge. Meta theory can also be viewed as a higher-order language bias that defines the hypothesis space. 

**PyGol** is a Python library that can be used in Python programs (e.g., Jupyter Notebooks). It can also connect with **SWI-Prolog** via **Janus**. 

**PyGol** is free to use for non-commercial research and education. If you use PyGol for research, please cite the paper: [Efficient Abductive Learning of Microbial Interactions using Meta Inverse Entailment](https://link.springer.com/chapter/10.1007/978-3-031-55630-2_10).
```cmd
Dany Varghese, Didac Barroso-Bergada, David A. Bohan  and  Alireza Tamaddoni-Nezhad, 
Efficient Abductive Learning of Microbial Interactions using Meta Inverse Entailment,  
In Proceedings of the 31st International Conference on ILP, Springer, 2022.
```
Anyone wishing to use PyGol for commercial purposes should contact either Dany Varghese(dany.varghese@surrey.ac.uk) or Alireza Tamaddoni-Nezhad(a.tamaddoni-nezhad@surrey.ac.uk).

## Contributions
* An ILP approach **Meta Inverse Entailment(MIE)**
* An algorithm to generate **Bottom Clause of Relevant Literals (BCRL)**
* A new **higher-order** language bias **Meta Theory (MT)** - Automatically generating from BCRL
* **Abductive Learning** using MIE
* Meta Inverse Entailment (MIE) for the purpose of **automated data science**

#### Requirements
* [SWI-Prolog](https://www.swi-prolog.org) (9.2.0 or above)
* [Janus-swi](https://github.com/SWI-Prolog/packages-swipy)
* [Cython](https://cython.org/)

## Using PyGol
**PyGol** package is provided as a **C** code. The shared-object file **pygol.so** runs in Python. The current shared-object file is compiled for **Mac M1** systems.

For all other systems, you can find the **C** code  and convert it to shared-object by executing the **generate_so.py** by following commands;

```cmd
python3 generate_so.py build_ext --inplace
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
model= pygol_learn(Train_P, Train_N,  max_neg=0, max_literals=3, key_size=1)
```

### Output from learning phase
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

## Recursion

PyGol is capable of learning recursive programs where a predicate symbol is present in both the rule's head and its body. 

To lean recursive rule, **recursive** and **rule_noise_check** variable should be set as True inside **pygol_learn()**. 

```Python
model= pygol_learn(_ ,_ , ... , rule_noise_check = True, recursive = True)
```

_Please refer to [ancestor relation learning problem](https://github.com/danyvarghese/PyGol/tree/main/examples/ancestor)._


## Predicate invention

PyGol can also perform automatic predicate invention and for that **pi** varibale should set as True. 

```Python
model= pygol_learn(_ ,_ , ... ,  pi = True)
```

_Please refer to [grandparent relation learning problem](https://github.com/danyvarghese/PyGol/tree/main/examples/grand_parent)._

## Learning settings
- ILP  Learning Approach :- **pygol_learn()**
- ILP Cross-Validation Approach :- **pygol_cross_validation()**
- ILP abduction (Reasoning) :- **pygol_abduction()**

For further information, please find the [manual](https://github.com/danyvarghese/PyGol/blob/debbe3024fda4cfaf33936e76dfd9455e455c39c/Manual_Pygol.pdf).

## Publications
* Didac Barroso-Bergada, Alireza Tamaddoni-Nezhad, Dany Varghese, Corinne Vacher, Nika Galic, Valérie Laval, Frédéric Suffert, David A Bohan. [Unravelling the web of dark interactions: Explainable inference of the diversity of microbial interactions](https://www.sciencedirect.com/science/article/abs/pii/S0065250423000053?via%3Dihub).  Advances in Ecological Research, 2023.
* Dany Varghese, Roman Bauer, Alireza Tamaddoni-Nezhad. [Few-Shot Learning of Diagnostic Rules for Neurodegenerative Diseases Using Inductive Logic Programming](https://link.springer.com/chapter/10.1007/978-3-031-49299-0_8). Lecture Notes in Computer Science, Springer, 2023.
*  Dany Varghese, Uzma Patel, Paul Krause & Alireza Tamaddoni-Nezhad. [Few-Shot Learning for Plant Disease Classification Using ILP](https://link.springer.com/chapter/10.1007/978-3-031-35641-4_26). Communications in Computer and Information Science, Springer, 2022.

## Bug reports and feature requests
Please submit all bug reports and feature requests as issues on this GitHub repository.
