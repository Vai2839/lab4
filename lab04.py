class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return team_matches

    def search_by_location(self, location_name):
        location_matches = [match for match in self.matches if match.location == location_name]
        return location_matches

    def search_by_timing(self, timing):
        timing_matches = [match for match in self.matches if match.timing == timing]
        return timing_matches

def main():
    table = FlightTable()

    # Adding matches to the table
    table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    print("Search Options:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")

    choice = int(input("Enter your choice: "))
   

    if choice == 1:
        print("Vaibhav Ahlawat E22CSEU0467")
        team_name = input("Enter team name: ")
        matches = table.search_by_team(team_name)
    elif choice == 2:
        print("Vaibhav Ahlawat E22CSEU0467")
        location_name = input("Enter location name: ")
        matches = table.search_by_location(location_name)
    elif choice == 3:
        print("Vaibhav Ahlawat E22CSEU0467")
        timing = input("Enter timing: ")
        matches = table.search_by_timing(timing)
    else:
        print("Vaibhav Ahlawat E22CSEU0467")
        print("Invalid choice")
        return

    if matches:
        print("Match Details:")
        for match in matches:
            print(f"Location: {match.location}, Team 1: {match.team1}, Team 2: {match.team2}, Timing: {match.timing}")
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
