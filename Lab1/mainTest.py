from atmFunction import deposit,with_draw, exchangeToUsd, exchangeToPln
# Test the deposit function
amount = 500
amount = deposit(amount, 100)
assert amount == 600

amount = 500
amount = deposit(amount, -100)
assert  amount == "Enter valid number of deposit"

# Test the withDraw function
amount = 500
amount = with_draw(amount, 200)
assert amount == 300

amount = -200
amount = with_draw(amount, 200)
assert amount == "No enough money"

amount = 500
amount = with_draw(amount, -200)
assert amount == "Enter correct number"

amount = 500
amount = with_draw(amount, 200)
assert amount == 300

amount = 500
amount = exchangeToUsd(amount)
assert amount == 112.35955056179775

amount = -500
amount = exchangeToPln(amount)
assert amount == "No money"

amount = 0
amount = exchangeToPln(amount)
assert amount == 0

amount = 112.35955056179775
amount = exchangeToPln(amount)
assert amount == 500


