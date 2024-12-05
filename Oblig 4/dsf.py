def jorgen(chips, wager):
    new_chips = chips - wager
    return new_chips


chips = 5
while chips > 0:
    global new_chips
    wager = 1
    print(chips)
    jorgen(chips, wager)
    chips = new_chips
