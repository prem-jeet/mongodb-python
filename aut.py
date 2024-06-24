from dotenv import load_dotenv
load_dotenv()

import os
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

from supabase import create_client, Client
if not key or not url:
  raise ValueError("url or key not found")


access_token = None
try:
    supabase = create_client(url,key)
    user_email: str = "jeet4300795@gmail.com"
    user_pass: str = "QAZ@#12df"

    credentials = {
    "email": user_email,
    "password": user_pass
    }

    user = supabase.auth.sign_in_with_password(credentials)
    acceess_token = user.session.access_token
except Exception as e:
  print(f"some error occured : {e}")
# res = supabase.storage.create_bucket("image")
# print(res)
filepath = "IMG_7095.jpeg"

try:
  with open(filepath, "rb") as f:
    res = supabase.storage.from_("image-bucket").upload(filepath, f,{"content-type": "image/*"})
    print(res)
except Exception as e:
  print(f"File error: {e}")

# res = supabase.storage.from_("image-bucket").upload("IMG_7096.png"); 
# print(res)


supabase.auth.sign_out();


