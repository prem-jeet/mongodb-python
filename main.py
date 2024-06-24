from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Retrieve the URL and key from the environment variables
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Check if the URL and key are loaded correctly
if not url or not key:
    raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in environment variables")

# Create a Supabase client 
supabase: Client = create_client(url, key) 

# Perform a query
try: 
   filepath = "IMG_7095.jpeg"
   bucket = "img"
#    with open(filepath, 'rb') as f:
        # res = supabase.storage.from_(bucket).upload(filepath,f,{"content-type": "image/*"})
        # print(res) 
   res = supabase.storage.from_(bucket).list();
   print(res)

except Exception as e:
    print(f"An error occurred: {e}")