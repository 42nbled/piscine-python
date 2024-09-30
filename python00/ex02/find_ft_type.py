# find_ft_type.py

def all_thing_is_obj(obj: any) -> int:
    
    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String",
        float: "Float",
        bool: "Boolean"
    }

    obj_type_name = type_names.get(type(obj), "Type not found")
    
    if obj_type_name == "String":
        print(f"{obj} is in the kitchen : <class '{type(obj).__name__}'>")
    elif obj_type_name != "Type not found":
        print(f"{obj_type_name} : <class '{type(obj).__name__}'>")
    else:
        print("Type not found")

    return 42
