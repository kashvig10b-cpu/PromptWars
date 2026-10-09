import urllib.request
import json
import time

api_base = "https://digital-skill-passport-api-production.up.railway.app/api"

# 1. Register student with JUST name "Kashvi"
email = f"kashvi_final_{int(time.time())}@dsp.edu"
reg_data = json.dumps({
    "name": "Kashvi",
    "email": email,
    "password": "Password123",
    "role": "student",
    "college": "Sapthagiri NPS University"
}).encode("utf-8")

req = urllib.request.Request(f"{api_base}/auth/register", data=reg_data, headers={"Content-Type": "application/json"})
res = urllib.request.urlopen(req)
body = json.loads(res.read())
token = body["token"]
print("Registered Kashvi successfully! Token obtained.")

# 2. Add technical skills, projects, and degree
update_data = json.dumps({
    "bio": "Full-Stack Software Engineer & AI Systems Developer specializing in React, Node.js, and Java DSA.",
    "degree": "B.Tech",
    "department": "Computer Science & Engineering",
    "location": "Bengaluru, India",
    "github": "https://github.com/kashvi",
    "linkedin": "https://linkedin.com/in/kashvi",
    "skills": [
        {"name": "React.js", "level": "Expert", "category": "Frontend"},
        {"name": "Node.js", "level": "Advanced", "category": "Backend"},
        {"name": "Java (DSA)", "level": "Expert", "category": "Core"},
        {"name": "MongoDB", "level": "Advanced", "category": "Database"},
        {"name": "Socket.IO", "level": "Advanced", "category": "Real-Time"}
    ],
    "projects": [
        {
            "title": "Digital Skill Passport",
            "description": "Real-time verified credential platform with QR telemetry & WebSocket synchronization.",
            "technologies": ["React", "Node.js", "MongoDB", "Socket.IO", "Java"],
            "liveUrl": "https://digital-skill-passport.vercel.app"
        },
        {
            "title": "Cloud Resume Engine",
            "description": "In-memory binary streaming platform with automated ATS parsing.",
            "technologies": ["Node.js", "Express", "Multer", "Docker"],
            "liveUrl": "https://github.com/kashvi"
        }
    ]
}).encode("utf-8")

req_up = urllib.request.Request(
    f"{api_base}/profile",
    data=update_data,
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"},
    method="PUT"
)
res_up = urllib.request.urlopen(req_up)
print("Profile populated with skills and projects! Response code:", res_up.status)

# Save credentials to a file for selenium
with open("student_creds.json", "w") as f:
    json.dump({"email": email, "password": "Password123", "token": token}, f)
print("Saved student_creds.json")
