                                                         Guessing Game
Player:
The Player is a standalone Python server that attempts to find the target number as quickly as possible and engages with the Game Master without any direct interaction.

Game Master:
The Game Master is a server capable of managing multiple game sessions simultaneously. It randomly selects a number within a specified range and responds with:
- "higher" if the guessed number is too low,
- "lower" if the guessed number is too high,
- "won" if the guessed number is correct.

Description:
As an outsider, you can initiate a new round and observe how the two entities interact. The numbers in play range from 1 to 1000.
The game can be accessed locally using Flask at http://localhost:8080/play.
This project served as my initial foray into learning Docker and Azure. Additionally, I have deployed the game as a Docker image to Azure Container Instances (ACI), set up an Azure Container Registry (ACR), and successfully run the game online.
