# HW 9.10
from restaurant import Restaurant
import users

my_rest = Restaurant('OnSeat', 'Columbian')
my_rest.describe_restaurant()
my_rest.open_restaurant()

# HW 9.11
admin = users.Admin('Joe', 'Spencer', '45', 'male', 'Administrator')
print("\n")
admin.greet_admin()
admin.privileges.show_privileges()