"""
Syntecxhub Internship - Project 2
Rule-Based Expert System

Educational demonstration of:
- Facts base
- If-then rules
- Forward chaining
- Multi-step inference
- Inference-step logging

This is a demonstration system, not a medical diagnostic tool.
"""

from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass(frozen=True)
class Rule:
    name: str
    conditions: Set[str]
    conclusion: str


RULES = [
    Rule(
        "Rule 1",
        {"fever", "cough"},
        "possible_respiratory_infection",
    ),
    Rule(
        "Rule 2",
        {"possible_respiratory_infection", "fatigue"},
        "recommend_rest_and_hydration",
    ),
    Rule(
        "Rule 3",
        {"sore_throat", "cough"},
        "possible_throat_irritation",
    ),
    Rule(
        "Rule 4",
        {"possible_throat_irritation", "fever"},
        "recommend_medical_evaluation",
    ),
    Rule(
        "Rule 5",
        {"headache", "fatigue"},
        "possible_general_illness",
    ),
    Rule(
        "Rule 6",
        {"possible_general_illness", "fever"},
        "recommend_medical_evaluation",
    ),
]


def normalize_fact(text: str) -> str:
    """Convert user input into a consistent fact format."""
    return text.strip().lower().replace(" ", "_")


def forward_chain(initial_facts: Set[str]) -> Tuple[Set[str], List[str]]:
    """
    Apply rules repeatedly until no new facts can be inferred.

    Returns:
        final_facts: all original and inferred facts
        inference_log: human-readable reasoning steps
    """
    facts = set(initial_facts)
    inference_log = []
    changed = True

    while changed:
        changed = False

        for rule in RULES:
            if rule.conditions.issubset(facts) and rule.conclusion not in facts:
                facts.add(rule.conclusion)
                inference_log.append(
                    f"{rule.name}: IF "
                    f"{', '.join(sorted(rule.conditions))} "
                    f"THEN {rule.conclusion}"
                )
                changed = True

    return facts, inference_log


def display_results(initial_facts: Set[str], final_facts: Set[str], log: List[str]) -> None:
    """Display facts, inference steps and conclusions."""
    print("\n========================================")
    print("     RULE-BASED EXPERT SYSTEM")
    print("========================================")

    print("\nInitial Facts:")
    for fact in sorted(initial_facts):
        print(f"  - {fact.replace('_', ' ')}")

    print("\nInference Steps:")
    if log:
        for number, step in enumerate(log, start=1):
            print(f"  {number}. {step.replace('_', ' ')}")
    else:
        print("  No rules were triggered.")

    new_facts = final_facts - initial_facts

    print("\nInferred Conclusions:")
    if new_facts:
        for fact in sorted(new_facts):
            print(f"  - {fact.replace('_', ' ')}")
    else:
        print("  No additional conclusions were inferred.")

    print("\nReasoning completed using forward chaining.")


def get_user_facts() -> Set[str]:
    """Collect facts/symptoms from the user."""
    print("\nEnter facts separated by commas.")
    print("Example: fever, cough, fatigue")
    raw = input("Facts: ")

    facts = {
        normalize_fact(item)
        for item in raw.split(",")
        if item.strip()
    }
    return facts


def main():
    print("Rule-Based Expert System")
    print("------------------------")

    initial_facts = get_user_facts()

    if not initial_facts:
        print("\nNo facts were entered. Please run the program again.")
        return

    final_facts, inference_log = forward_chain(initial_facts)
    display_results(initial_facts, final_facts, inference_log)


if __name__ == "__main__":
    main()
