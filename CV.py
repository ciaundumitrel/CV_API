class CV:
    def __init__(self, personal=None, skills=None, education=None, experience=None, projects=None, languages=None, hobbies=None):
        """
        :param personal:
        :param skills:
        :param experience:
        :param projects:
        :param languages:
        :param hobbies:
        """
        self.personal = personal
        self.skills = skills
        self.experience = experience
        self.education = education
        self.projects = projects
        self.languages = languages
        self.hobbies = hobbies


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
