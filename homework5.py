immutable_var = ('String', 10, True, [1, 3, False])
print(immutable_var)
immutable_var[3][1] = "Mod" #Изменять элементы кортежа нельзя. В данном кортеже, можно изменить элеименты только во вложенном списке
mutable_list = [135, True, 34, 'Text']
mutable_list[2] = [2, 'New element']
print(mutable_list)
