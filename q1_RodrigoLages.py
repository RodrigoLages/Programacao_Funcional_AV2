accLogin = {
    "Zale": "sun123",
    "Valerie": "moon321",
    "Garl": "b35t_c00k"
}
accAmmount = {
    "Zale": 500,
    "Valerie": 605,
    "Garl": 1230
}

start = lambda l, p, q, a: checkAcc(l, p, q, wtdr) if a == "W" else checkAcc(l, p, q, dpst) if a == "D" else print("Operation not supported")

checkAcc = lambda l, p, q, f: print("Login Error") if accLogin[l] != p else f(l, q)

wtdr = lambda l, q: print("Withdraw not allowed") if accAmmount[l] < q else updateAcc(l, -q)
dpst = lambda l, q: updateAcc(l, q)

updateAcc = lambda l, q: accAmmount.update({l: accAmmount[l] + q})


start("Zale", "1234", 50, "W")
start("Zale", "sun123", 50, "W")
start("Valerie", "moon321", 700, "W")
start("Valerie", "moon321", 70, "W")
start("Garl", "b35t_c00k", 270, "S")
start("Garl", "b35t_c00k", 270, "D")
print(accAmmount)