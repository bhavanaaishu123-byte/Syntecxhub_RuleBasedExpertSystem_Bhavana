# ==========================================
# RULE-BASED EXPERT SYSTEM USING PYTHON
# ==========================================

# Welcome Message
print("====================================")
print("   RULE-BASED EXPERT SYSTEM")
print("====================================")
print("Enter symptoms separated by commas")
print("Example: fever, cough, body_pain")
print()


# ==========================================
# RULES DATABASE
# ==========================================
# Each rule contains:
# "if"  -> conditions
# "then" -> conclusion

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


# ==========================================
# USER INPUT SECTION
# ==========================================

# Take symptoms from user
user_input = input("Enter symptoms: ")

# Convert input into lowercase
# and split using comma
facts = user_input.lower().split(",")

# Remove extra spaces
facts = [fact.strip() for fact in facts]


# ==========================================
# FORWARD CHAINING FUNCTION
# ==========================================

def forward_chaining(facts, rules):

    # Store newly inferred facts
    inferred = []

    # Store reasoning steps
    steps = []

    # Loop until no new facts are added
    while True:

        # Track whether a new fact is added
        new_fact_added = False

        # Check each rule
        for rule in rules:

            # Check if all conditions are present
            if all(condition in facts for condition in rule["if"]):

                # Avoid duplicate conclusions
                if rule["then"] not in facts:

                    # Add new inferred fact
                    facts.append(rule["then"])

                    # Store inferred fact
                    inferred.append(rule["then"])

                    # Log reasoning step
                    steps.append(
                        f"Applied rule: IF {rule['if']} THEN {rule['then']}"
                    )

                    # Mark that a new fact was added
                    new_fact_added = True

        # Stop loop if no new facts added
        if not new_fact_added:
            break

    # Return final facts and reasoning steps
    return facts, steps


# ==========================================
# RUN EXPERT SYSTEM
# ==========================================

final_facts, steps = forward_chaining(facts, rules)


# ==========================================
# DISPLAY INFERENCE STEPS
# ==========================================

print("\n====================================")
print("       INFERENCE STEPS")
print("====================================")

if steps:
    for step in steps:
        print(step)
else:
    print("No matching rules found.")


# ==========================================
# DISPLAY FINAL CONCLUSIONS
# ==========================================

print("\n====================================")
print("       FINAL CONCLUSIONS")
print("====================================")

for fact in final_facts:
    print("-", fact)


# ==========================================
# DISPLAY MOST POSSIBLE CONDITION
# ==========================================

print("\n====================================")
print("     MOST POSSIBLE CONDITION")
print("====================================")

# Show the last inferred fact
print(final_facts[-1])

print("\nThank you for using the Expert System!")