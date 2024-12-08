# Write your solution here
'''
There are two JSON files: partial.json and all.json. The first of these is mostly 
meant for testing. The latter contains a lot of data, as all the NHL player stats 
for the 2019-20 season are included in the file.
'''
import json

class FileHandler:
    def __init__(self, filename):
        self.__filename = filename
        self.data = self.load_file()

    # Load json file
    def load_file(self): 
        with open(self.__filename) as file:
            players = json.load(file)
        return players
    
    def count_obj(self):
        return len(self.data)
    
        
class ProcessData:
    '''
    Process data from all.json OR partial.json file to match commands in Application
    '''
    def __init__(self, name: str, data):
        self.name = name
        self.data = data
    
    # Return team for referenced player
    def get_player_team(self): 
        return next(player["team"] for player in self.data if player["name"] == self.name)
    
    # Return goals for referenced player
    def get_player_goals(self): 
        return next(player["goals"] for player in self.data if player["name"] == self.name)
        
    def get_player_assists(self):
        return next(player["assists"] for player in self.data if player["name"] == self.name)
    
    # Command 2: return list of teams in data
    def get_teams(self): 
        return[player["team"] for player in self.data] # list comprehension

        #same result as generator
        '''
        seen_teams = set() 
        for player in self.data:
            team = player['team']
            if team not in seen_teams:
                seen_teams.add(team)
                yield team
        '''
    
    # Command 3: return list of countries in data   
    def get_countries(self): 
        return[player["nationality"] for player in self.data]
    
    # Command 4: return players in a specific team in the order of points scored, from highest to lowest
    def players_in_team(self, team): 
        def order_by_points(player: dict):
            points = player["goals"] + player["assists"]
            return points
        
        # List of players from team sorted by most goals scored 
        sorted_players = sorted(self.data, key=order_by_points, reverse=True)
        for player in sorted_players:
            if player['team'] == team:
                yield str(ProcessData(player["name"], self.data))
    
    # Command 5: list of players sorted by points for the country mentioned
    def players_from_country(self, country):
        def order_by_points(player: dict):
            points = player["goals"] + player["assists"]
            return points
        
        # List of players from country sorted by most goals scored 
        sorted_players = sorted(self.data, key=order_by_points, reverse=True)
        for player in sorted_players:
            if player['nationality'] == country:
                yield str(ProcessData(player["name"], self.data))
    
    # Return list of players sorted by points    
    def sort_by_most_points(self, num_players): 
        # Helper function
        def order_by_points(player: dict):
            points = player["goals"] + player["assists"]
            return (points, player["goals"])
        
        # Return list of top players based on num_players called
        top_players = sorted(self.data, key=order_by_points, reverse=True)[:num_players]
        return [str(ProcessData(player["name"], self.data)) for player in top_players]
    
    def sort_by_most_goals(self, num_players):
        # Helper function
        def order_by_goals(player: dict):
            return(player["goals"], -player["games"])
        
        # Return list of top players based on num_players called
        top_players = sorted(self.data, key=order_by_goals, reverse=True)[:num_players]
        return [str(ProcessData(player["name"], self.data)) for player in top_players]
    
    
    def __str__(self):
        '''
        Return f string formatted with correct spacing:
        Markus Granlund      EDM   3 +  1 =   4
        123456789012345678901234567890123456789
        '''
        name = self.name
        team = self.get_player_team()
        goals = self.get_player_goals()
        assists = self.get_player_assists()
        return f"{name:<21}{team:<5}{goals:>2} +{assists:>3} = {goals + assists:>3}"
    

class HockeyDataApplication:
    '''
    Application "user interface" for processing hockey data
    '''
    def __init__(self):
        self.file_data = None
    
    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
        
    def execute(self):
        file_name = input('file name: ')
        file_handler = FileHandler(file_name)
        self.file_data = file_handler.load_file()
        count = FileHandler(file_name).count_obj()
        print(f'read the data of {count} players ')
        print("")
        self.help()
        while True:
            print()
            try:
                command = int(input("command: "))
                if command == 0:
                    break
                elif command == 1:
                    self.player_search()
                elif command == 2:
                    self.teams()
                elif command == 3:
                    self.countries()
                elif command == 4:
                    self.players_in_teams()
                elif command == 5:
                    self.players_from_country()
                elif command == 6:
                    self.most_points()
                elif command == 7:
                    self.most_goals()
                else:
                    self.help()
            except ValueError:
                print('Please enter a numbered command between 0-7')
        
    def player_search(self): # command 1
        name = input("name: ")
        try:
            player = ProcessData(name, self.file_data)
            print(player)
        except StopIteration:
            print(f"Player {name} not found.")
    
    def teams(self): # command 2
        data = ProcessData(None, self.file_data)
        for team in sorted(set(data.get_teams())):
            print(team)
    
    def countries(self): # command 3
        data = ProcessData(None, self.file_data)
        for country in sorted(set(data.get_countries())):
            print(country)
    
    def players_in_teams(self): # command 4
        team = input("team: ")
        try:
            print("")
            data = ProcessData(None, self.file_data)
            team_found = False
            for player in data.players_in_team(team):
                print(player)
                team_found = True
            if not team_found:
                print(f"Team {team} not found.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
    def players_from_country(self): # command 5
        country = input("country: ")
        try:
            print("")
            data = ProcessData(None, self.file_data)
            country_found = False
            for player in data.players_from_country(country):
                print(player)
                country_found = True
            if not country_found:
                print(f"Country {country} not found.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def most_points(self): # Command 6
        quantity = int(input("how many: "))
        try:
            print("")
            data = ProcessData(None, self.file_data)
            players_found = False
            for player in data.sort_by_most_points(quantity):
                print(player)
                players_found = True
            if not players_found:
                print(f"Invalid entry")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def most_goals(self): # Command 7
        quantity = int(input("how many: "))
        try:
            print("")
            data = ProcessData(None, self.file_data)
            players_found = False
            for player in data.sort_by_most_goals(quantity):
                print(player)
                players_found = True
            if not players_found:
                print(f"Invalid entry")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        
app = HockeyDataApplication()
app.execute()
