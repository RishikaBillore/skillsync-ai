from flask import Flask, request

app = Flask(name)

roles = {

"backend developer": [
    "java",
    "spring boot",
    "sql",
    "jwt",
    "rest api",
    "redis",
    "microservices",
    "docker",
    "git"
],

"frontend developer": [
    "html",
    "css",
    "javascript",
    "react",
    "tailwind css",
    "redux",
    "git",
    "responsive design"
],

"full stack developer": [
    "html",
    "css",
    "javascript",
    "react",
    "node js",
    "express js",
    "mongodb",
    "sql",
    "git"
],

"data analyst": [
    "python",
    "excel",
    "sql",
    "power bi",
    "statistics",
    "tableau"
],

"data scientist": [
    "python",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pandas",
    "numpy",
    "statistics"
],

"machine learning engineer": [
    "python",
    "machine learning",
    "tensorflow",
    "pytorch",
    "feature engineering",
    "model deployment",
    "docker",
    "sql"
],

"android developer": [
    "java",
    "kotlin",
    "android studio",
    "firebase",
    "xml",
    "rest api"
],

"devops engineer": [
    "linux",
    "docker",
    "kubernetes",
    "jenkins",
    "aws",
    "terraform",
    "git",
    "ci/cd"
],

"cybersecurity analyst": [
    "network security",
    "ethical hacking",
    "linux",
    "cryptography",
    "wireshark",
    "penetration testing",
    "python"
],

"ui ux designer": [
    "figma",
    "wireframing",
    "prototyping",
    "user research",
    "design systems"
],

"cloud engineer": [
    "aws",
    "azure",
    "google cloud",
    "docker",
    "kubernetes",
    "linux",
    "terraform"
],

"blockchain developer": [
    "solidity",
    "ethereum",
    "smart contracts",
    "web3",
    "javascript",
    "cryptography"
]

}

@app.route("/", methods=["GET", "POST"])
def home():

result = ""

if request.method == "POST":

    user_skills = request.form["skills"].lower().split(",")

    target_role = request.form["role"].lower()

    user_skills = [skill.strip() for skill in user_skills]

    required_skills = roles.get(target_role, [])

    if not required_skills:

        result = """
        <h2>Role not found!</h2>
        <p>Please enter a valid role.</p>
        """

    else:

        missing_skills = []

        for skill in required_skills:

            if skill not in user_skills:
                missing_skills.append(skill)

        result += "<h2>Skill Gap Analysis</h2>"

        if missing_skills:

            result += "<h3>Missing Skills:</h3>"

            for skill in missing_skills:
                result += f"<p>• {skill.title()}</p>"

        else:

            result += """
            <h3>You already have all required skills!</h3>
            """

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
            max-width: 500px;
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
        }}

    </style>

</head>

<body>

    <div class="container">

        <h1>SkillSync AI</h1>

        <p>Analyze your skill gaps for different tech roles.</p>

        <form method="POST">

            <label>Enter Your Skills:</label>

            <input
                type="text"
                name="skills"
                placeholder="Example: Java, SQL, REST API"
                required
            >

            <label>Enter Target Role:</label>

            <input
                type="text"
                name="role"
                placeholder="Example: Backend Developer"
                required
            >

            <button type="submit">
                Analyze Skills
            </button>

        </form>

        <br>

        {result}

    </div>

</body>

</html>

"""

app.run(host="0.0.0.0", port=5000)
