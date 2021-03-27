# fruit_name - weight in kgs - cost
fruits_quantity = [['apples', 1, 100], ['oranges', 1.5, 60], ['grapes', 0.5, 120]]

total_cost = 0.0
for fruit in fruits_quantity:
    #print(fruit, 'name:', fruit[0], 'weight:', fruit[1], 'cost:', fruit[2])
    weight = fruit[1]
    rate = fruit[2]
    cost = weight * rate
    total_cost += cost

print('total cost:', total_cost)