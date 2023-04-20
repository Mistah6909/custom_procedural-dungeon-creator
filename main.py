import random
import time

seed_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 1, 2, 3, 4, 5, 6, 7,8, 9, 0]
seed = ""
x_iterator = 1
for x in range(12):
  seed = seed + str(random.choice(seed_chars))
random.seed(seed)
print("set the room weight this will affect the amount of rooms that are generated in the level or you can leave it empty(max room weight is 5 default room weight is 2)")
room_weight = 3
y_iterator = 0
surrounding_rooms = 0

max_rooms = random.randint(5, 10) * room_weight
if max_rooms >110:
  max_rooms = 110
print(max_rooms)
print("the seed used for this generation is " + seed)
row1 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row2 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row3 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row4 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row5 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row6 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row7 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row8 = ["0", "0", "0", "0", "0", "0", "0", "0", "O", "0", "0", "0", "0", "0", "0", "0", "0"]
row9 = ["0", "0", "0", "0", "0", "0", "0", "O", "S", "O", "0", "0", "0", "0", "0", "0", "0"]
row10 =["0", "0", "0", "0", "0", "0", "0", "0", "O", "0", "0", "0", "0", "0", "0", "0", "0"]
row11 =["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row12 =["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row13 =["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row14 =["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row15 =["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row16 =["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
row17 =["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11,row12,row13,row14,row15,row16,row17]
rooms = 1
surrounding_rooms = 0
while rooms < max_rooms:
  for row in rows:
    x_iterator = 0
    for thing in row:
      abv_weight = random.uniform(0,1)
      lft_weight = random.uniform(0,1)
      rht_weight = random.uniform(0,1)
      blw_weight = random.uniform(0,1)
      weight_vals = [abv_weight,lft_weight,rht_weight,blw_weight]
      try:
        tpl = rows[y_iterator-1][x_iterator-1]
        abv = rows[y_iterator - 1][x_iterator]
        tpr = rows[y_iterator - 1][x_iterator + 1]
        lft = rows[y_iterator][x_iterator - 1]
        rht = rows[y_iterator][x_iterator + 1]
        btr = rows[y_iterator + 1][x_iterator -1]
        blw = rows[y_iterator + 1][x_iterator]
        btl = rows[y_iterator + 1][x_iterator + 1]
        surroundings = [tpl,abv,tpr,lft,rht,btl,blw,btr]
        surrounding_rooms = 0
        for room in surroundings:
          if room == "O":
            surrounding_rooms += 1  
        if rows[y_iterator][x_iterator] == "O":
          if max(weight_vals) == abv_weight:
            if rows[y_iterator-1][x_iterator ] != "S" and surrounding_rooms <= 3:
              rows[y_iterator-1][x_iterator] = "O"
          if max(weight_vals) == lft_weight :
            if rows[y_iterator][x_iterator-1] != "S" and surrounding_rooms <= 3:
              rows[y_iterator][x_iterator-1] = "O"
          if max(weight_vals) == rht_weight:
            if rows[y_iterator][x_iterator + 1] != "S" and surrounding_rooms <= 3:
              rows[y_iterator][x_iterator + 1] = "O"
          if max(weight_vals) == blw_weight:
            if rows[y_iterator + 1][x_iterator] != "S" and surrounding_rooms <= 3:
              rows[y_iterator + 1][x_iterator] = "O"
          rooms += 1
        x_iterator += 1

      except IndexError:
        if y_iterator > 17:
          y_iterator = 0
          rooms = 1
    y_iterator += 1
y_iterator = 0
x_iterator = 0
for row in rows:
  x_iterator = 0
  for thing in row:
    if thing == "0":
      rows[y_iterator][x_iterator] = " "
    x_iterator += 1
  y_iterator += 1
for x in rows:
  print(x)
