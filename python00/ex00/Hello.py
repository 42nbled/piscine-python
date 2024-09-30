ft_list = ["Hello", "tata!"]    # is equal to list
ft_tuple = ("Hello", "toto!")   # is equal to const
ft_set = {"Hello", "tutu!"}     # is equal to stack
ft_dict = {"Hello" : "titi!"}   # is equal to map

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(sorted(ft_set))
print(ft_dict)