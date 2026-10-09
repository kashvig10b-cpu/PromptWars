import urllib.request
import json
import time

api_base = "https://digital-skill-passport-api-production.up.railway.app/api"

# 1. Register a fresh recruiter
rec_email = f"recruiter_live_{int(time.time())}@techcorp.com"
reg_payload = json.dumps({
    "name": "Sarah Connor",
    "email": rec_email,
    "password": "Password123",
    "role": "recruiter",
    "company": "TechCorp Global",
    "companyWebsite": "https://techcorp.com"
}).encode("utf-8")

req = urllib.request.Request(f"{api_base}/auth/register", data=reg_payload, headers={"Content-Type": "application/json"})
res = urllib.request.urlopen(req)
body = json.loads(res.read())
rec_id = body["user"]["id"]
print(f"Registered Recruiter: {rec_email} (ID: {rec_id})")

# 2. Login as Admin to approve this recruiter
admin_login = json.dumps({"email": "admin@dsp.gov", "password": "admin123"}).encode("utf-8")
req_ad = urllib.request.Request(f"{api_base}/auth/login", data=admin_login, headers={"Content-Type": "application/json"})
res_ad = urllib.request.urlopen(req_ad)
admin_token = json.loads(res_ad.read())["token"]

# 3. Approve recruiter
approve_payload = json.dumps({"recruiterStatus": "APPROVED"}).encode("utf-8")
req_app = urllib.request.Request(
    f"{api_base}/admin/recruiters/{rec_id}",
    data=approve_payload,
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {admin_token}"},
    method="PUT"
)
res_app = urllib.request.urlopen(req_app)
print(f"Approved Recruiter status: {res_app.status}")

# Save recruiter credentials for Selenium
with open("recruiter_creds.json", "w") as f:
    json.dump({"email": rec_email, "password": "Password123"}, f)
print("Saved recruiter_creds.json!")
