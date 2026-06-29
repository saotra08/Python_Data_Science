ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

ft_list[1] = "World!"
ft_tuple = ft_tuple[:1] + ("Madagascar!",)
ft_set.discard("tutu!")
ft_set.add("Antananarivo!")
ft_dict['Hello'] = '42Antananarivo!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
