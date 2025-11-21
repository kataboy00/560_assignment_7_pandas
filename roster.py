# https://goheels.com/sports/mens-basketball/roster
import pandas as pd
roster =["Evans", "High", "Brown"]
player = {"Last Name": roster,
          "First Name": ["Kyan", "Zayden", "James"],
          "height": [74, 82, 82],
          "weight": [175, 230, 240]}
data = pd.DataFrame(player)
print(data)