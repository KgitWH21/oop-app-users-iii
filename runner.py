from users import User
from users import FreeUser
from users import PremiumUser

free_user = FreeUser("John", "John@email.com")
premium_user = PremiumUser("Alice", "Alice@email.com")

print(free_user, premium_user)