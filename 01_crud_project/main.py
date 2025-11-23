from tables import create_table
from services import create_user, create_post, get_user_by_id, get_all_users, get_post_by_user_id, update_user_email


# Create tables 
# create_table()


# User
# create_user("Talha Rana", "example@gmail.com")
# create_user("Shahjahan Talha", "shahjahan@gmail.com")
# print(get_all_users())

# print(get_user_by_id(1))

update_user_email(1,"taharana@gmail.com")


# Post
# create_post(1, "How AI Effect on Online fields", "5 effected fields by AI ")
# create_post(2, "AI automation in 2025", "powerful skill in 2025 AI is the best and top skill in 2025")

# print(get_post_by_user_id(2))


