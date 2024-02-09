import operator
import BlindAuctionArt
import os


print(BlindAuctionArt.logo)

continue_action = False
bidders = {}
def find_highest_bidder(bidding_record):
    highest_bidding=0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidding:
            highest_bidding =bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidding}")

while not continue_action:
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: $"))
    bidders[user_name] = user_bid
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if add_bidders.lower() == "no":
        continue_action = True
        find_highest_bidder(bidders)
    elif add_bidders.lower() == "yes":
        os.system('cls')
