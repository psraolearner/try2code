unconfirmed_users = ["siv","srinu","venky","sai","vijay"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user:"+ current_user.title())

    confirmed_users.append(current_user)

print("\n The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print("Confirmed users: "+ confirmed_user.title())

    
    
