import pdb

def make_bricks(small, big, goal):
  # small bricks = 1 in
  # big bricks = 5 in
  bLength = big * 5
  # return goal <= (small+bLength)

  #if the goal can just be made out of big bricks available
  # if ((goal%5 == 0) & (goal/5 <= big)):
  #   return True
  # else if ((goal
  savegoal = goal
  savebig = big
  savesmall = small

  while (savegoal > 0):
    if ((savegoal >= 5) & (savebig > 0)):
      savegoal -= 5
      savebig -= 1
    elif ((savegoal >= 0) & (savesmall > 0)):
      savegoal -= 1
      savesmall -= 1
    elif ((savesmall == 0) & (savegoal > 0)):
      return False
    # pdb.set_trace()
  return (savegoal == 0)

  # #first subtract the largest bricks one by one
  # goal -= 5
  # big -= 1
  # #until there are no more big bricks
  # stop when big == 0
  # #OR goal is smaller than 5
  # goal <= 5
  # #then subtract the small bricks one by one
  # goal -= 1
  # small -= 1
  # #until there are no more small bricks
  # stop when small == 0
  # #OR goal is less than or equal to 0
  # goal <= 0
  # #return true if goal == 0 or false if goal != 0

  # if (goal == 0):
  #   return True
  # elif (goal <= 0):
  #   return False
  # else:
  #   if ((goal > 5) & (big > 0)):
  #     goal -= 5
  #     big -= 1
  #   #   make_bricks(small,big,goal)
  #   elif ((goal > 0) & (small > 0)):
  #     goal -= 1
  #     small -= 1
    #   make_bricks(small,big,goal)

print make_bricks(3,2,9)
print make_bricks(3,2,10)
print make_bricks(2,4,18)
