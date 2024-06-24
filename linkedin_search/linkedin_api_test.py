from linkedin_api import Linkedin
import pandas as pd
from credentials import LINKEDIN_USER, LINKEDIN_PASSWORD



# Authenticate using any Linkedin account credentials
api = Linkedin(LINKEDIN_USER, LINKEDIN_PASSWORD)

res = api.search_people(keywords='HWR', limit=10)
first = res[0]['name']

first = api.get_profile(first)
print(first)



