print("====================================")
print("   RULE-BASED EXPERT SYSTEM")
print("====================================")
print("Enter symptoms separated by commas")
print("Example: fever, cough, body_pain")
print()


rules = [
    {"if": ["fever", "cough"], "then": "flu"},
    {"if": ["flu", "body_pain"], "then": "viral_infection"},
    {"if": ["headache", "fever"], "then": "migraine"},
    {"if": ["sneezing", "runny_nose"], "then": "cold"},
    {"if": ["cold", "fever"], "then": "infection"},
    {"if": ["chest_pain", "breathlessness"], "then": "heart_problem"},
    {"if": ["stomach_pain", "vomiting"], "then": "food_poisoning"},
    {"if": ["fever", "rash"], "then": "allergy"}
]

user_input = input("Enter symptoms: ")
facts = user_input.lower().split(",")
facts = [fact.strip() for fact in facts]
def forward_chaining(facts, rules):

    inferred = []

    steps = []

    while True:

        new_fact_added = False
        for rule in rules:
            if all(condition in facts for condition in rule["if"]):
                if rule["then"] not in facts:
                    facts.append(rule["then"])
                    inferred.append(rule["then"])

                    steps.append(
                        f"Applied rule: IF {rule['if']} THEN {rule['then']}"
                    )
                    new_fact_added = True
        if not new_fact_added:
            break
    return facts, steps

final_facts, steps = forward_chaining(facts, rules)

print("\n====================================")
print("       INFERENCE STEPS")
print("====================================")

if steps:
    for step in steps:
        print(step)
else:
    print("No matching rules found.")
print("\n====================================")
print("       FINAL CONCLUSIONS")
print("====================================")

for fact in final_facts:
    print("-", fact)
print("\n====================================")
print("     MOST POSSIBLE CONDITION")
print("====================================")
print(final_facts[-1])

print("\nThank you for using the Expert System!")
