def ground_shipping(weight):
  if weight < 2:
    cost = weight * 1.5 + 20
  elif weight > 2 and weight < 6:
    cost = weight * 3 + 20
  elif weight > 6 and weight < 10:
    cost = weight * 4 + 20
  else:
    cost = weight * 4.75 + 20
  return cost
print(ground_shipping(8.4))

cost_premium_ground_shipping = 125

def drone_shipping(weight):
  if weight < 2:
    cost = weight * 4.5
  elif weight > 2 and weight < 6:
    cost = weight * 9
  elif weight > 6 and weight < 10:
    cost = weight * 12
  else:
    cost = weight * 14.25
  return cost
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = cost_premium_ground_shipping
  drone = drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone
  
  print(
    "The cost of shipping this package is $%.2f. The cheapest shipping method is: %s."
    % (cost, method)
  )

# testing:
cheapest_shipping(4.8)
cheapest_shipping(41.5)
