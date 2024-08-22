import google.generativeai as genai
import os
import credentials

genai.configure(api_key= credentials.login["key"])

model = genai.GenerativeModel('gemini-1.5-flash')