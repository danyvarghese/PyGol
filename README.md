# PyGol
PyGol is novel Inductive Logic Programming(ILP) system based on **Meta Inverse Entailment(MIE)**.  MIE is similar to Mode-Directed Inverse Entailment (MDIE) but does not require mode declarations.

PyGol has written in **Python**(Learning Phase) and, during the test phase, uses **Pyswip** to have fare analysis with logic programming. 

## Contributions
* An ILP approach **Meta Inverse Entailment(MIE)**
* An algorithm to generate **Meta Clause Set(MCS) **
* Defining Most Speific Clause using MCS
* A new **higher-order** language bias **Meta Theory(MT)** - Automatically generating from MCS
* **Abductive Learning** using MIE
* Meta Inverse Entailment (MIE) for the purpose of automated data science

## Using PyGol
The shared object file** pygol.so** runs in Python. We have converted the basic _Pygol_ code to _C_ code via _Cython_ for efficiency. The current shared-object file is compiled for **Linux x86_64** systems. 

for all other systems, you can find the c code in the folder Cython_code and convert it to shared-object by executing the following commands;

```cmd
gcc <Python_Environment_Variable> -c -fPIC pygol.c -o pygol.o
gcc pygol.o -shared -o pygol.so
```



