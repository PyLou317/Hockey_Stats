# NHL Player Statistics Application

## Overview

### (Project is a work in progress and not 100% completed)

This Python application provides a comprehensive interface for analyzing NHL player statistics from JSON data files. It allows users to explore player information, team details, and performance metrics for the 2019-20 NHL season.

## Features

- 🏒 Player search functionality
- 📊 Team and country information retrieval
- 🏆 Ranking players by points and goals
- 🔍 Flexible data processing and exploration

## Project Structure

The application consists of several key classes:

1. **FileHandler**: 
   - Loads JSON files containing player statistics
   - Provides a secure method for file reading

2. **ProcessData**: 
   - Processes and analyzes player data
   - Provides methods for:
     * Retrieving player teams
     * Calculating goals and penalties
     * Sorting players by performance
     * Listing teams and countries

3. **HockeyDataApplication**: 
   - Provides a command-line interface for interacting with the data
   - Supports multiple commands for data exploration

## Prerequisites

### Requirements
- Python 3.7+
- Standard library modules:
  - `json`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nhl-stats-app.git
   cd nhl-stats-app
   ```

2. Ensure you have the required JSON files:
   - `partial.json`
   - `all.json`

## Usage

Run the application:
```bash
python hockey_stats_app.py
```

### Available Commands
- `0`: Quit the application
- `1`: Search for a specific player
- `2`: List all teams
- `3`: List all countries
- `4`: List players in a specific team
- `5`: List players from a specific country
- `6`: Show players with the most points (goals + assists)
- `7`: Show players with the most goals

## Example Workflow

1. Launch the application
2. View available commands using the help menu
3. Enter a command number
4. Follow the prompts to explore NHL player statistics

## Data Format

The application expects JSON files with the following player data structure:
```json
{
  "name": "Player Name",
  "team": "Team Abbreviation",
  "goals": 10,
  "assists": 15,
  "penalties": 5,
  "nationality": "Country"
}
```

## Customization

- Modify `ProcessData` class to add more complex statistical analysis
- Extend `HockeyDataApplication` to include additional commands
- Update JSON parsing logic in `FileHandler` as needed

## Potential Improvements

- Add error handling for invalid inputs
- Implement more advanced filtering and sorting
- Create a graphical user interface (GUI)
- Support multiple season data files

## Limitations

- Currently supports only JSON file formats
- Designed for the 2019-20 NHL season data
- Command-line interface only

## Contact

Lucas Patriquin: lucas.patriquin@gmail.com
