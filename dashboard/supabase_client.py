import os
from dotenv import load_dotenv
from supabase import create_client, Client
from django.conf import settings


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
