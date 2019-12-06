#https://adventofcode.com/2019/day/4

def availablepasswords(lb, ub):
  results = []
  
  for pw in range(lb, ub + 1):
    pw = str(pw)
    result = []
    duplicateflag = False

    for i in range(0,len(pw)):
      digit = int(pw[i])
      if i == 0:
        result.append(digit)
      elif digit >= result[len(result) - 1]:
        if digit == result[len(result) - 1]:
          duplicateflag = True
        
        result.append(digit)
      else:
        break
    
    if len(pw) == len(result) and duplicateflag == True:
      results.append(result)
      print(results[len(results)-1])
  
  return results

def main():
  passwords = availablepasswords(278384,824795)
  print(len(passwords))

if __name__ == "__main__":
  main()