# Syntecxhub Project 2 — Rule-Based Expert System

## Objective

Build a small rule engine using if-then rules and a facts base. The system accepts user facts, performs inference using forward chaining, supports multi-step inference, and logs the inference steps so the reasoning path can be viewed.

These requirements directly match the Project 2 description in the Syntecxhub internship task.

## Technology

- Python 3.8+
- Standard Python library only
- No external packages required

## Project Structure

```text
Syntecxhub_Rule_Based_Expert_System/
├── main.py
├── README.md
├── sample_output.txt
└── LinkedIn_Post.txt
```

## How to Run

Open a terminal in this folder:

```bash
python main.py
```

Then enter facts separated by commas.

Example:

```text
fever, cough, fatigue
```

## Main Concepts

### 1. Facts Base

Facts are represented as strings, for example:

```text
fever
cough
fatigue
```

The facts entered by the user form the initial facts base.

### 2. If-Then Rules

Rules contain:

```text
IF conditions
THEN conclusion
```

For example:

```text
IF fever AND cough
THEN possible_respiratory_infection
```

### 3. Forward Chaining

The system starts with known facts and repeatedly checks the rules.

If all conditions of a rule are present, its conclusion is added to the facts base. The process continues until no new conclusion can be produced.

### 4. Multi-Step Inference

The system supports chaining.

For example:

```text
fever + cough
       ↓
possible respiratory infection
       ↓ + fatigue
recommend rest and hydration
```

The second rule can use the conclusion produced by the first rule.

### 5. Inference Log

Every rule that fires is recorded and displayed. This allows the user to see the reasoning path.

## Example

Input:

```text
fever, cough, fatigue
```

The system can infer:

```text
possible respiratory infection
recommend rest and hydration
```

The inference log shows which rules produced those conclusions.

## Important Note

The example rules use symptom-like facts only to demonstrate the expert-system mechanism. They are not intended to provide medical diagnosis or treatment advice.

## Requirement Checklist

- Small rule engine: **Completed**
- If-then rules: **Completed**
- Facts base: **Completed**
- Accept user facts: **Completed**
- Forward chaining: **Completed**
- Multi-step inference: **Completed**
- Inference-step logging: **Completed**
