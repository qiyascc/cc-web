from reactpy import component, html, run
import requests
import aiohttp
import asyncio
##########################################################################
userData = {
    "name": "Qiyas Sadıqov",
    "profession": "Software Engineer",
    "shortBio": "I can code anything you can think of. 🧑‍💻",
    "socialLinks": {
        "github": "https://github.com/qiyascc",
        "instagram": "https://instagram.com/qiyascc",
        "linkedin": "https://linkedin.com/in/qiyascc",
        "telegram": "https://t.me/qiyascc"
    },
    "aboutText": "Detailed about section text. Important part of the text.",
    "experience": [
        {
            "dateRange": "May 2023 - June 2023",
            "title": "CEO & Software Engineer",
            "description": "LaFood.",
            "technologies": ['Node.Js', 'MongoDB', 'Express', 'Dart']
        },
        {
            "dateRange": "Mart 2021 - Present",
            "title": "Freelance",
            "description": "Fullstack software engineer",
            "technologies": ['Node.js', 'SQL', 'PostCSS', 'C++', 'React Native', 'jQuery', 'Telethon', 'React.js', 'JavaScript', 'CSS', 'HTML5']
        },
        {
            "dateRange": "MDec 2023 - Present",
            "title": "CEO & Technical Lead",
            "description": "Chaplean.",
            "technologies": ['Sales Management', 'Project Management', 'Software Project Management', 'CEO']
        },
    ],
    "projects": [
        {
            "title": "TexnoPark.com (V1, V2, V3)",
            "description": "The purpose of this site is to promote the technopark within the Western Caspian University and to provide certain services to the university students.",
            "imageUrl": "https://texnopark.com/static/images/topImages/navbarAndFooter/logo.png",
            "technologies": ['Nginx', 'gunicorn', 'JSON', 'Django', 'Bootstrap', 'SQLite', 'Express.js', 'Python', 'jQuery', 'JavaScript', 'CSS', 'HTML5']
        },
        {
            "title": "Service Manager",
            "description": "You can monitor and manage your services with this telegram bot. Simple and functional.",
            "imageUrl": "https://texnopark.com/static/images/topImages/navbarAndFooter/logo.png",
            "technologies": ['telegraf', 'Node.js', 'JavaScript']
        },
        {
            "title": "Bestfixappliances.COM",
            "description": "It is a basic website for the repair company serving globally. It works as an alternative. The website belongs to me as a fullstack. I used html, css (tailwindcss), additional js libraries and django in the project.",
            "imageUrl": "https://texnopark.com/static/images/topImages/navbarAndFooter/logo.png",
            "technologies": ['HTML', 'tailwindCSS', 'JavaScript', 'Django']
        },
    ],
    "writings": [
        {
            "imageUrl": "https://via.placeholder.com/160x90",
            "date": "2023",
            "title": "Writing Title",
            "link": "https://example.com"
        }
    ]
}

@component
def UserProfile():
    userProfile = userData

    about_section = html.div({"class": "mt-8"},
        html.h2({"class": "text-2xl"}, "About"),
        html.p({"id": "aboutContent", "class": "text-sm mt-2 text-whiteish-gray"}, userProfile["aboutText"])
    )
    social_links_section = html.div({"class": "flex mt-4"},
        [html.a({"id": f"{key}Link", "href": value, "class": "mr-4", "key": f"social-link-{key}"}, html.i({"class": f"bi bi-{key}"}))
         for key, value in userProfile["socialLinks"].items()]
    )
    experience_section = html.div({"class": "mt-8", "key": "experience-section"},
        html.h2({"class": "text-2xl"}, "Experience"),
        html.div({"id": "experienceSection", "class": "mt-4"},
            [html.div({"class": "mt-4 mb-10", "key": f"experience-{index}"},
                html.p({"class": "text-sm text-whiteish-gray"}, exp["dateRange"]),
                html.h3({"class": "text-xl font-semibold"}, exp["title"]),
                html.p({"class": "text-base text-whiteish-gray"}, exp["description"]),
                html.div({"class": "flex flex-wrap mt-2"},
                    [html.span({"class": "technology-item rounded-full px-3 py-1 text-sm font-semibold mr-2 mb-2", "key": f"tech-{index}-{tech_index}"}, tech)
                    for tech_index, tech in enumerate(exp["technologies"])]
                )
            ) for index, exp in enumerate(userProfile["experience"])]
        )
    )
    projects_section = html.div({"class": "mt-8", "key": "projects-section"},
        html.h2({"class": "text-2xl"}, "Projects"),
        html.div({"id": "projectsSection", "class": "mt-4"},
            [html.div({"class": "mb-10", "key": f"project-{index}"},
                html.h3({"class": "text-xl font-semibold"}, project["title"]),
                html.p({"class": "text-base text-whiteish-gray"}, project["description"]),
                html.div({"id": f"projectImageContainer-{index}", "class": "w-1/2 mt-4 bg-cover bg-center", "style": {"backgroundImage": f"url('{project['imageUrl']}')"}}),
                html.div({"class": "flex flex-wrap mt-2"},
                    [html.span({"class": "technology-item rounded-full px-3 py-1 text-sm font-semibold mr-2", "key": f"project-tech-{index}-{tech_index}"}, tech)
                     for tech_index, tech in enumerate(project["technologies"])]
                )
            ) for index, project in enumerate(userProfile["projects"])]
        )
    )
    writing_section = html.div({"class": "mt-8", "key": "writing-section"},
        html.h2({"class": "text-2xl"}, "Writing"),
        html.div({"id": "writingSection", "class": "mt-4"},
            [html.div({"class": "flex items-center mb-2.5", "key": f"writing-{index}"},
                html.div({"class": "w-20 aspect-w-16 aspect-h-9 mr-2"},
                    html.img({"src": writing["imageUrl"], "alt": "Writing Image", "class": "w-full h-full object-cover"})
                ),
                html.div({},
                    html.p({"class": "text-sm text-whiteish-gray"}, writing["date"]),
                    html.a({"href": writing["link"], "class": "text-base text-lavander"}, writing["title"])
                )
            ) for index, writing in enumerate(userProfile["writings"])]
        )
    )

    ## HTML ##
    return html.div({"class": "container mx-auto px-4"},
            html.div({"class": "pt-8"},
                html.h1({"id": "name", "class": "text-3xl font-bold"}, userProfile["name"]),
                html.p({"id": "profession", "class": "text-xl mt-2"}, userProfile["profession"]),
                html.p({"id": "shortBio", "class": "text-base mt-1 text-whiteish-gray"}, userProfile["shortBio"]),
                social_links_section,
                about_section,
                experience_section,
                projects_section,
                writing_section
            )
    )

# async def main():
#     user_data = await get_user_data()
#     run(lambda: UserProfile(user_data))

# asyncio.run(main())