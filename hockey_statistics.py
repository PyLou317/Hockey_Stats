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
        
    def get_player_penalties(self):
        return next(player["penalties"] for player in self.data if player["name"] == self.name)
    
    # Return list of teams in data
    def get_teams(self): 
        return[player["team"] for player in self.data]
    
    # Return list of countries in data   
    def get_countries(self): 
        return[player["nationality"] for player in self.data]
    
    # List players in a specific team in the order of points scored, from highest to lowest
    def players_in_team(self, team): 
        return[player["name"] for player in self.data if player["team"] == team]
    '''Need to correct'''
    
    # Return list of players sorted by points    
    def sort_by_most_points(self, num_players): 
        # Helper function
        def order_by_points(player: dict):
            points = player["goals"] + player["assists"]
            return points
        
        # Return list of top players based on num_players called
        top_players = sorted(self.data, key=order_by_points, reverse=True)[:num_players]
        return [str(ProcessData(player["name"], self.data)) for player in top_players]
    
    def sort_by_most_goals(self, num_players):
        # Helper function
        def order_by_goals(player: dict):
            return player["goals"]
        
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
        penalties = self.get_player_penalties()
        return f"{name:<21}{team:<5}{goals:>2} + {penalties:>2} = {goals + penalties:>2}"
    


class HockeyDataApplication:
    '''
    Application "user interface" for processing hockey data
    '''
    def __init__(self):
        self.__hockeydata = ProcessData(None, FileHandler.load_file)
    
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
        self.help()
        print()
        command = int(input("command: "))
        
        if command == 0:
            quit
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
            return # add error handling for anything not a int 0-7
        
    def player_search(self):
        ...
    
    def teams(self):
        ...
    
    def countries(self):
        ...
    
    def players_in_teams(self):
        ...
    
    def players_from_country(self):
        ...
    
    def most_points(self):
        ...
    
    def most_goals(self):
        ...
        
        

'''data = FileHandler("all.json")
processed_data = ProcessData(None, data.data)
top_players = processed_data.sort_most_points(10)
for player in top_players:
    print(player)'''
    
app = HockeyDataApplication()
app.execute()
    
# res = PlayerData("Andy Greene")
# print(res.get_team())