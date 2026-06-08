from flask import Flask, request

app = Flask(__name__)

roles = {
    "backend developer": [
        "java", "spring boot", "sql", "jwt", "rest api",
        "redis", "microservices", "docker", "git", "system design"
    ],

    "frontend developer": [
        "html", "css", "javascript", "react",
        "tailwind css", "redux", "git", "responsive design",
        "typescript"
    ],

    "full stack developer": [
        "html", "css", "javascript", "react",
        "node js", "express js", "mongodb", "sql",
        "git", "rest api", "authentication"
    ],

    "data analyst": [
        "python", "excel", "sql", "power bi",
        "statistics", "tableau", "data visualization",
        "pandas"
    ],

    "data scientist": [
        "python", "statistics", "machine learning",
        "pandas", "numpy", "scikit learn",
        "data cleaning", "feature engineering"
    ],

    "devops engineer": [
        "linux", "docker", "kubernetes", "jenkins",
        "aws", "ci/cd", "git", "terraform",
        "monitoring"
    ],

    "android developer": [
        "java", "kotlin", "android studio",
        "xml", "firebase", "rest api",
        "git"
    ],

    "ios developer": [
        "swift", "xcode", "ios sdk",
        "swiftui", "rest api", "git"
    ],

    "machine learning engineer": [
        "python", "machine learning", "deep learning",
        "tensorflow", "pytorch", "numpy",
        "pandas", "model deployment"
    ],

    "cybersecurity analyst": [
        "networking", "linux", "penetration testing",
        "cryptography", "firewalls", "security tools",
        "risk analysis"
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":

        # input cleaning (VERY IMPORTANT FIX)
        user_skills = request.form["skills"].lower()
        user_skills = [skill.strip() for skill in user_skills.split(",")]

        target_role = request.form["role"].lower().strip()

        required_skills = roles.get(target_role, [])

        if not required_skills:
            result = """
            <h2>❌ Role not found!</h2>
            <p>Please enter a valid role from the list.</p>
            """

        else:
            missing_skills = [
                skill for skill in required_skills
                if skill not in user_skills
            ]

            result = "<h2>📊 Skill Gap Analysis</h2>"

            if missing_skills:
                result += "<h3>❌ Missing Skills:</h3>"
                for skill in missing_skills:
                    result += f"<p>• {skill.title()}</p>"
            else:
                result += "<h3>🎉 You already have all required skills!</h3>"

    return f"""
    <html>
    <head>
        <title>SkillSync AI</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f4f4;
                padding: 40px;
            }}

            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                max-width: 550px;
                margin: auto;
                box-shadow: 0px 0px 10px gray;
            }}

            input {{
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                margin-bottom: 20px;
            }}

            button {{
                padding: 10px 20px;
                background-color: black;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}

            button:hover {{
                background-color: #333;
            }}

        </style>
    </head>

    <body>
        <div class="container">
            <h1>SkillSync AI 🚀</h1>
            <p>Analyze your skill gaps for tech roles.</p>

            <form method="POST">

                <label>Your Skills:</label>
                <input type="text" name="skills"
                    placeholder="Java, SQL, REST API" required>

                <label>Target Role:</label>
                <input type="text" name="role"
                    placeholder="backend developer" required>

                <button type="submit">Analyze</button>
            </form>

            <br>
            {result}
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
