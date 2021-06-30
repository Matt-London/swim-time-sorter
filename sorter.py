import sys

from obj.Person import Person
from obj.Collection import Collection

AGE_GROUPS = ["-1 8", "9 10", "11 12", "13 14", "15 -1"]

collection = Collection(sys.argv[1])

for group in AGE_GROUPS:
    groupS = "-".join(group.split(" "))
    # ================ Male ====================
    collection.get_group(group, "m")

    # Fly
    collection.sort_stroke(0)
    collection.export(groupS + "_m")

    # Back
    collection.sort_stroke(1)
    collection.export(groupS + "_m")

    # Breast
    collection.sort_stroke(2)
    collection.export(groupS + "_m")

    # free
    collection.sort_stroke(3)
    collection.export(groupS + "_m")

    # ================ Female ====================
    collection.get_group(group, "f")

    # Fly
    collection.sort_stroke(0)
    collection.export(groupS + "_f")

    # Back
    collection.sort_stroke(1)
    collection.export(groupS + "_f")

    # Breast
    collection.sort_stroke(2)
    collection.export(groupS + "_f")

    # free
    collection.sort_stroke(3)
    collection.export(groupS + "_f")
