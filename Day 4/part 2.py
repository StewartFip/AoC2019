#https://adventofcode.com/2019/day/4#part2

def availablepasswords(lb, ub):
  results = []
  
  for pw in range(lb, ub + 1):
    pw = str(pw)
    result = []
    duplicateflag = False
    duplicatecount = 0

    for i in range(0,len(pw)):
      digit = int(pw[i])
      if i == 0:
        result.append(digit)
      elif digit >= result[len(result) - 1]:
        if digit == result[len(result) - 1]:
          duplicatecount += 1
        else:
          if duplicatecount == 1:
            duplicateflag = True
          duplicatecount = 0
        
        result.append(digit)
      else:
        break
    
    if len(pw) == len(result) and (duplicateflag == True or duplicatecount == 1):
      results.append(result)
      #print(results[len(results)-1])
  
  return results

def main():
  #456 is too low
  passwords = availablepasswords(278384,824795)
  #passwords = availablepasswords(111122,111122)
  print(len(passwords))

if __name__ == "__main__":
  main()