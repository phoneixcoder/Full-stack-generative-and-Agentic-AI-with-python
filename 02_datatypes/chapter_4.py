is_boiling = True
stir_count = 0

total_actions = stir_count + is_boiling #upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # or none will give you false
print(f"Milk present: {bool(milk_present)}")