register = lambda username, password: open("q2_data.txt", "a").write(username + " " + password + "\n")

login = lambda username, password: "SUCCESS" if checkCred(open("q2_data.txt").read().split("\n"), username, password) else "FAILURE"

checkCred = lambda users, username, password: any(map(lambda u: u.split(" ")[0] == username and u.split(" ")[1] == password, users))

print(login("user", "123"))
register("user", "123")
print(login("user", "123"))
