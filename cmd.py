import click
import requests

from CV import hard_coded_data

API_URL = "http://127.0.0.1:3000"

@click.command("display")
@click.argument('name')
def commands(name):
    hobbies = []
    personal = {}
    skills = []
    education = []
    projects = []
    experience = []
    languages = []

    if "hobbies" in name:
        try:
            hobbies = requests.get(API_URL + "/get/hobbies").json()
            print(hobbies)
        except requests.exceptions.Timeout as err:
            print(f"Failed getting hobbies data {err}")
    elif "personal" in name:
        try:
            personal = requests.get(API_URL + "/get/personal").json()
            print(personal)
        except requests.exceptions.Timeout as err:
            print(f"Failed getting personal data {err}")
    elif "skill" in name:
        try:
            skills = requests.get(API_URL + "/get/skills").json()
            print(skills)
        except requests.exceptions.Timeout as err:
            print(f"Failed getting skills data {err}")
    elif "education" in name:
        try:
            education = requests.get(API_URL + "/get/education").json()
            print(education)
        except requests.exceptions.Timeout as err:
            print(f"Failed getting education data {err}")
    elif "projects" in name:
        try:
            projects = requests.get(API_URL + "/get/projects").json()
            print(projects)
        except requests.exceptions.Timeout as err:
            print(f"Failed getting projects data {err}")

    elif "experience" in name:
        try:
            experience = requests.get(API_URL + "/get/experience").json()
            print(experience)
        except requests.exceptions.Timeout as err:
            print(f"Failed experience hobbies data {err}")
    elif "languages" in name:
        try:
            languages = requests.get(API_URL + "/get/languages").json()
            print(languages)
        except requests.exceptions.Timeout as err:
            print(f"Failed getting languages data {err}")

    elif "all" in name:
        try:
            hobbies = requests.get(API_URL + "/get/hobbies").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed getting hobbies data {err}")

        try:
            personal = requests.get(API_URL + "/get/personal").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed getting personal data {err}")

        try:
            skills = requests.get(API_URL + "/get/skills").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed getting skills data {err}")

        try:
            education = requests.get(API_URL + "/get/education").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed getting education data {err}")
        try:
            projects = requests.get(API_URL + "/get/projects").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed getting projects data {err}")
        try:
            experience = requests.get(API_URL + "/get/experience").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed experience hobbies data {err}")
        try:
            languages = requests.get(API_URL + "/get/languages").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed getting languages data {err}")

        try:
            skills = requests.get(API_URL + "/get/skills").json()
        except requests.exceptions.Timeout as err:
            print(f"Failed getting skills data {err}")

        print(f"Hobbies:{hobbies} \n Personal Information:{personal} \n Skills: {skills} \nEducation : {education} \n  Projects:{projects} \n Experience:{experience} \n Languages:{languages}\n")
    else:
        print("Unrecognized command")

if __name__ == '__main__':
    commands()
