spice_mix = set()
print(f"initial spice mix: {id(spice_mix)}")


# It is mutable, so we can change the value of the object without changing the reference.
spice_mix.add("cumin")
print(f"spice mix after adding cumin: {id(spice_mix)}")

print(f"spice mix after adding cumin: {spice_mix}")

