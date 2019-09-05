# PrivateJobMatch

A repository containing many components used to build and test PrivateJobMatch using Python 2.7

---

## Dataset Generator

- Small script to generate synthetic candidate-employer preferences using the function *createDatasets* in [Dataset_Generator.py](a)
- Preferences are reasonably decided based on a utility function (assigned type).
- Specify the number of candidates and employers, *n* and *m* respectively.

---

## Job Market Simulator

- Code for simulating a job market.
- Employers offer jobs to candidates using a descending order of candidate priority, which can be inputted in the form of:
  - Raw preferences (as used in today's decentralized job market).
  - MMDAA match output (centralized job market).

---

## Low-Rank Matrix Factorization

- Code for performing LMF on a ***sparse*** dataset. See [LMF_Runner.py](a)
- Included a utility function, *sparsifyDataset*, for converting a dense dataset into a sparse dataset.

---

## Multi-Match Deferred Acceptance Algorithm

- [MMDAA.py](a) contains functions for various tasks.
- *setUpInputFile* will create a text file in the required format/structure for parsing when setting up the data structures (preprocessing) for running the MMDAA.
  - See [exampleInput.txt]() for required preference structure.
  - Takes two dense preference files (CSV format) as input. Outputs a text file.
- *mainRunner* loads the input text file that holds the required preference data, and runs the MMDAA. Saves the output in CSV files, as well as a text file.
- *runMetric* is a function used to select a metric to calculate, given match outputs and preference inputs.

---

## Results

- A folder containing experimental results (displacement, withholdings, vacancy) in the form of spreadsheets for various datasets.

---
