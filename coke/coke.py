def main():
    accepted_coins = {25, 10, 5}
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in accepted_coins:
            amount_due -= coin

    print(f"Change Owed: {-amount_due}")

if __name__ == "__main__":
    main()      
