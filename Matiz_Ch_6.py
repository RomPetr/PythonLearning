'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}."

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Пришелец перемещается вправо
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3

# Новая позиция равна сумме старой позиции и приращивания
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)
'''
# HW 6.1
human_0 = {'first_name': 'alex', 'last_name': 'corvin', 'age': '30', 'city': 'Denver'}
print(f"The first name of this human is {human_0['first_name'].title()}.")
print(f"The last name is {human_0['last_name'].title()}")
print(f"His age is {human_0['age']}.")
print(f"And he lives in {human_0['city']}.")
