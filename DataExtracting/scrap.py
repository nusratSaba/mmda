import requests
import beautifulsoup4 as bs
import json

url = "https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450"
response = requests.get(url)
soup = bs(response.content, "html.parser")
match_results_table = soup.find("table", class_="table table-striped table-bordered match-table")

match_results = []

for row in match_results_table.find_all("tr"):
    columns = row.find_all("td")

    match_result = {
        "date": columns[0].text,
        "team1": columns[1].text,
        "team2": columns[2].text,
        "result": columns[3].text,
    }

    match_results.append(match_result)

with open("match_results.json", "w") as f:
    json.dump(match_results, f)




