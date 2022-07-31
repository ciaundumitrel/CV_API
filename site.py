from flask import Flask, render_template
import requests


from CV import CV

app = Flask(__name__)

API_URL = "http://127.0.0.1:3000"


@app.route('/')
def display_cv():
    hobbies = []
    personal = {}
    skills = []
    education = []
    projects = []
    experience = []
    languages = []

    try:
        hobbies = requests.get(API_URL + "/get/hobbies").json()
    except Exception as err:
        print(f"Failed getting hobbies data {err}")

    try:
        personal = requests.get(API_URL + "/get/personal").json()
    except Exception as err:
        print(f"Failed getting personal data {err}")

    try:
        skills = requests.get(API_URL + "/get/skills").json()
    except Exception as err:
        print(f"Failed getting skills data {err}")

    try:
        education = requests.get(API_URL + "/get/education").json()
    except Exception as err:
        print(f"Failed getting education data {err}")
    try:
        projects = requests.get(API_URL + "/get/projects").json()
    except Exception as err:
        print(f"Failed getting projects data {err}")
    try:
        experience = requests.get(API_URL + "/get/experience").json()
    except Exception as err:
        print(f"Failed experience hobbies data {err}")
    try:
        languages = requests.get(API_URL + "/get/languages").json()
    except Exception as err:
        print(f"Failed getting languages data {err}")

    cv_data = CV(personal, skills, education, experience, projects, languages, hobbies)

    return render_template("index.html", content=cv_data)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
