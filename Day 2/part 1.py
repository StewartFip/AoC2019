#https://adventofcode.com/2019/day/2

def processintcode(code, inputvalues):
  if inputvalues[code] == 1:
    inputvalues[inputvalues[code + 3]] = inputvalues[inputvalues[code + 1]] + inputvalues[inputvalues[code + 2]]
  elif inputvalues[code] == 2:
    inputvalues[inputvalues[code + 3]] = inputvalues[inputvalues[code + 1]] * inputvalues[inputvalues[code + 2]]
  else:
    print("error encountered")

def main():
  #inputvalues = [1,9,10,3,2,3,11,0,99,30,40,50]
  #250703 is incorrect
  inputvalues = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]
  inputvalues[1] = 12
  inputvalues[2] = 2

  for i in range(0, len(inputvalues), 4):
    if inputvalues[i] == 99:
      print("encountered 99 at ", i)
      break
    else:
      processintcode(i, inputvalues)

  print(inputvalues)

if __name__ == "__main__":
  main()