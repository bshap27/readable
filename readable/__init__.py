from prettytable import PrettyTable

def readable(obj, cols = []):  
  x = PrettyTable(cols)
  for o in obj:
    x.add_row([getattr(o, c) for c in cols])
  return print(x)