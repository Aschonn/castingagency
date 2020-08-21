# This file should be included in .gitignore to not store sensitive data in version control
import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN" : "aschonn.us.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "casting"
}

DATABASE_URL = "postgres://lrkdvdlwfppuyp:1ee332efc9f47d343dd61a6a6050170264e2ab4e2d271dd8d72d4dbb06fd4ba9@ec2-54-156-121-142.compute-1.amazonaws.com:5432/d3sn99v9vjcb5n"

database_setup = {
   "database_name_production" : "castingagency",
   "user_name" : "postgres", # default postgres user name
   "password" : "091297", # if applicable. If no password, just type in None
   "port" : "localhost:5432" # default postgres port
}

pagination = {
    "example" : 10 # Limits returned rows of API
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA2R0JBMmgydUFfTVJRdWZ4bnhGSCJ9.eyJpc3MiOiJodHRwczovL2FzY2hvbm4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjY2ZTY5YTE1YjdiMDAxMzYxYTcwMiIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE1OTc5NzY0ODEsImV4cCI6MTU5ODA2Mjg4MSwiYXpwIjoiWk5neFU5Z3h1RnFWSm1wNXpLN2NyMkRjNkhMNG50MHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.dnVaO1asQ65lDapEZ8vq92Z7JZEXWcGHVOWDC4_gKO42kqZ-tWiuoO_jaf4SrxVChIzodOEbS9iHKjszn2RhSy10vTHq1OyKOxlJabtNftcJb7JRREV7-ypud5CgBkIzvtiSEfaM9q88pET1vi3t8IW4cR6bIL0rWAoeq49CPFdV7-HyUFi2Uow1ALpKrho9Qo8SPVkp9NTZjykx7I4De6sRfWsATEW-a_Uu5hxiXG0JQ3DOzta_Us93W6PWVTV230KWVfpTHbLktF37t10asgCFAXQz1Gc1WO6Y0lJcWjUQQshF13NLPiwsy7mHFn2jLRz3YXsjTSxBQqiDnD2XMA",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA2R0JBMmgydUFfTVJRdWZ4bnhGSCJ9.eyJpc3MiOiJodHRwczovL2FzY2hvbm4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjY2ZTY5YTE1YjdiMDAxMzYxYTcwMiIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE1OTc5NzY5OTAsImV4cCI6MTU5ODA2MzM5MCwiYXpwIjoiWk5neFU5Z3h1RnFWSm1wNXpLN2NyMkRjNkhMNG50MHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.C2VYwHqhGWzMOSqyepP9SI6DZx5zkMPuD76UOlk9KwmXPCcpFCReslq8xOuaTSkK6AofhPybjCcGx4thuc76RhkFJ8VxPeJgKbz5U-gK2AENCj6jSUpHbs4AQsbUj6t0ui_XKUb187IBP6_-qiGE4Cx2nNC2DxVmeQGWbLgz8IlA_cAiW4IzCpdr31ITUWoBcYdjhQ91MYTOm11fyxgDMgBkt3YSKFMeM8uGP04-Pf0KUHVIubGMWIrJNGwzcj-cxcu5D4TRaVFwldX54-ciwWI1pRQi5fYd9yYMJFujdd-xOhRDjCu3C-PBlL46zNk2mrRZtFXXSrJoYiPuoiZlhA",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjA2R0JBMmgydUFfTVJRdWZ4bnhGSCJ9.eyJpc3MiOiJodHRwczovL2FzY2hvbm4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjY2ZTY5YTE1YjdiMDAxMzYxYTcwMiIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE1OTc5NzcwNzQsImV4cCI6MTU5ODA2MzQ3NCwiYXpwIjoiWk5neFU5Z3h1RnFWSm1wNXpLN2NyMkRjNkhMNG50MHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.3kCSe7k_hETy33NCD97S7m32rqY4faTjnJ6TmweKPZWADQ-NP3ocOLCaadBGzAdez30vhMLochHSSQbgdEI50fYoSGE2ZrVsEGih1TE2WTxMjMFKCSmvHeunAq-Q8Rb3YmzRO6eITaZkiEj8FdFsM9_7s2joHoKPlpUcNB184-7tuaFeuOOLXT4G9V0WQqikbMIzK6SE2KgfZ9VmnSvRU2QRZF9LSYKabj_XzvtUNNc535k_FveWR_g7KA_4w4cPTs2il6_QkmQWAWpDdYkHY46sh1XEmMWHxO8pDqi6P1ZYgIPTiYKBgkCdDc_Wf3JboH8ftUYiCAjrMbgNPEsy1w"
}

#https://aschonn.us.auth0.com/authorize?audience=casting&response_type=token&client_id=ZNgxU9gxuFqVJmp5zK7cr2Dc6HL4nt0p&redirect_uri=http://127.0.0.1:8080