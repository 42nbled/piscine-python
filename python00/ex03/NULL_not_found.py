import math

def NULL_not_found(obj: any) -> int:

    null_types = {
        None: "Nothing",
        float("NaN"): "Cheese",
        0: "Zero",
        '': "Empty"
    }
    
    if obj in :
        print(f"{null_types[obj]}: {obj} <class '{type(obj).__name__}'>")
        return 0
    elif isinstance(obj, float)null_types and math.isnan(obj):
        print(f"Cheese: {obj} <class '{type(obj).__name__}'>")
        return 0
    else:
        print("Type not Found")
        return 1
