from atmFunction import with_draw, deposit, showAmount, exchangeToUsd, exchangeToPln

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_running = True
    is_pln = True
    amount = 500
    print("Welcome in our ATM")
    print("Your balance is ")
    showAmount(amount)
    while(is_running):

        print("1-show balance")
        print("2-deposit")
        print("3-withdraw")
        if is_pln:
            print("4-exchange to USD")
        else:
            print("4-exchange to PLN")
        input_a = int(input())
        if input_a == 1:
            showAmount(amount)
        if input_a == 2:
            print("How many you want to deposit?")
            input_b = int(input())
            amount = deposit(amount,input_b)
            print("succefully added balance is :")
            showAmount(amount)
        if input_a == 3:
            print("How many you want to withdraw?")
            input_c = int(input())
            amount = with_draw(amount, input_c)
            print("Your amount is ")
            showAmount(amount)
        if input_a == 4 and is_pln:
            print("Your dolars:")
            amount = exchangeToUsd(amount)
            print(amount)
            is_pln = False
        elif input_a == 4 and is_pln==False:
            print("Your Pln:")
            amount = exchangeToPln(amount)
            print(amount)
            is_pln = True
