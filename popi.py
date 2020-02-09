import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SportsProj.settings')
import django
django.setup()


from cricket.models import team

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = "https://www.icc-cricket.com/rankings/mens/team-rankings/test"
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

# RANKINGS
def populate():
	teams = page_soup.findAll("tr", {"class": "table-body"})
	for x in teams:
		team_info = x.text.split()
		team_rating = team_info.pop()
		team_points = team_info.pop()
		team_matches = team_info.pop()
		team_rank = team_info.pop(0)
		team_name = " ".join(team_info)
		new_team = team.objects.get_or_create(t_type = "test",rank = team_rank, name = team_name, matches = team_matches, points= team_points, rating = team_rating)[0]

def delet():
	team.objects.all().delete()

if __name__ == "__main__":
	print("Setting TEST data")
	delet()