#q2 escolhida

import os
from flask import Flask, request, render_template
app = Flask(__name__, template_folder="q5_templates_folder")

register = lambda username, password: (open("q5_data.txt", "a").write(username + " " + password + "\n"), "SUCCESS")[1]
login = lambda username, password: "SUCCESS" if checkCred(open("q5_data.txt").read().split("\n"), username, password) else "FAILURE"
checkCred = lambda users, username, password: any(map(lambda u: u.split(" ")[0] == username and u.split(" ")[1] == password, users))


reqresp_login = lambda : login ( f'{request.form["username"]}', f'{request.form["password"]}') if request.method == 'POST' else render_template('login.html')

reqresp_register = lambda : register (f'{request.form["username"]}', f'{request.form["password"]}') if request.method == 'POST' else render_template('register.html')

app.add_url_rule('/login/', 'login', reqresp_login, methods=['GET', 'POST'])
app.add_url_rule('/register/', 'register', reqresp_register, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=5000)