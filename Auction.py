import art
def comparison(our_bids):
    winning_amt = 0
    winner = ""
    for key in our_bids:
        bidder_amt = our_bids[key]
        if bidder_amt > winning_amt:
            winning_amt = bidder_amt
            winner = key
    print(f"The winner is {winner} with {winning_amt}")

auction_over=False
auction={}

while not auction_over:
    bidder=input("What is ur name?")
    bidamt=int(input("What is ur bid?"))
    auction[bidder]=bidamt
    more_bid=input("Are there any other bidders? Type 'yes' or 'no'").lower()

    print("\n"*100)

    if more_bid=='no':
        auction_over=True
        comparison(auction)
