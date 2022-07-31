
from flask import Flask
from flask_restful import Api, Resource
from CV import CV

app = Flask(__name__)
api = Api(app)


class API(Resource):
    def __init__(self, curriculum_vitae):
        self.cv = curriculum_vitae

    def get(self, name):

        if name == "personal":
            return self.cv.personal

        elif name == "skills":
            return self.cv.skills

        elif name == "education":
            return self.cv.education

        elif name == "experience":
            return self.cv.experience

        elif name == "projects":
            return self.cv.projects

        elif name == "languages":
            return self.cv.languages

        elif name == "hobbies":
            return self.cv.hobbies


hard_coded_data = CV(
    personal={"name": "Ciaun Dumitrel", "job": "Software Developer", "address": "str. Ionel Teodoreanu",
              "email": "ciaundumitrel@gmail.com", "phone": "0741742634",
              "links": "https://www.linkedin.com/in/ciaun-dumitrel-961a18175/"},
    skills=["python", "web developement", "flexibility", "problem solving", "algorithmic thinking",
            "self-management"],
    education=[{"school": "Liceul Teoretic Alexandru Ioan Cuza", "begin": "Sep 2014", "end": "Jun 2018",
                "profile": "Stiinte ale Naturii"},
               {"school": "Universitatea Aleaxandru Ioan Cuza", "begin": "Oct 2021", "end": "Jul 2024",
                "profile": "Computer Science"}],
    experience=[{"jobTitle": "Software Developer", "company": "Continental", "begin": "Apr 2021", "end": "present",
                 "description": ["developed the interfaces for tools in Python using PyQt5 connected to large data bases",
                                 "Updated already in use tools",
                                 "worked with experienced developers and learned good coding practices",
                                 "worked with automotive related hardware",
                                 "Developed new tools and programs in Python"]},
                ],
    projects=[{"name": "Face detection and recognition application", "languages": ["Python", "PyQt5", "OpenCV"],
               "description": "Application that detects and recognize faces and send email t me when a face is detected."},
              {"name": "Store management application", "languages": ["Python", "PyQt5", "MySQL"],
               "description": "GUI Applicaiton that stores data shop in a MySQL data base"},
              {"name": "Lung Radiography Application", "languages": ["Python", "PyQt5", "OpenCV", "pydicom"],
               "description": "Application that can zoom into lung radiography and can detect lung problems using deep learning"},
              {"name": "Remote Control Prohibition", "languages": ["Python", "PyQt5"],
               "description": "Application that locks control over PC stations that are under maintenance"},
              {"name": "Tools Checker", "languages": ["Python"],
               "description": "Application that checks all software versions from the PC station"},
              {"name": "A2L Editor, merger and shrinker", "languages": ["Python"],
               "description": "Application that can edits .a2l files, merges or shrinks them."},
              {"name": "Syntax highlighter", "languages": ["HTML, CSS, JavaScript"],
               "description": "Application that can edits .a2l files, merges or shrinks them."},
              ],
    languages=["english", "romanian"],
    hobbies=["football", "books", "history", "movies"])

api.add_resource(API, "/get/<string:name>", resource_class_kwargs={"curriculum_vitae": hard_coded_data})

if __name__ == '__main__':

    app.run(debug=True, port=3000)
