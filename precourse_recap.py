age = 15
if age >= 15:
    print("Enjoy the ride on the rollercoaster!")
else:
    print("You are not old enough to ride this attraction.")



def cupcake_count(inner, outer):
    result = inner * outer
    return result
print(cupcake_count(6,12))

def cost_of_cupcakes(inner, outer):
    result = cupcake_count(inner, outer) * 2.25
    return result
print(cost_of_cupcakes(4,10))

