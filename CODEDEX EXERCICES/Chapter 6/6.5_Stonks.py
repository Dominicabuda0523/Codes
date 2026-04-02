# Write code below 💖

stock_prices = [
  34.68, 36.09, 34.94, 33.97, 34.68, 
  35.82, 43.41, 44.29, 44.65, 53.56, 
  49.85, 48.71, 48.71, 49.94, 48.53, 
  47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

print(price_at(1))

def max_prices(a, b):
  return max(stock_prices[a-1:b+1])

print(max_prices(1,5))

def min_prices(a, b):
  return min(stock_prices[a-1:b+1])



print(min_prices(1,5))
