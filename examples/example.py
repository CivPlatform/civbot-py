# prompts Microsoft authentication which determines the account used
bot = Bot("mcserver.example.com")

try:
    # use window while it"s open
    with bot.open_block_window(chest_location, face="top") as win:
        # methods can be called without await, even if they take time (client-server-communication)
        win.deposit(42, "stone")
# if the server closes the window while it"s being used
# (for example, a chest gets broken),
# the code inside `with` gets interrupted with an error
except WindowClosed as event:
    handle_closed(event)
else:
    handle_deposit_success()

# the remaining code demonstrates ideas
# which may or may not be included in the future

# do something until some event happens, then interrupt
try:
    with bot.interrupt_on_event(HealthChange, lambda event: event.health < 10):
        do_stuff()
except HealthChange as event:
    handle_hurt(event.health)
    # it"s up to the script developer to decide how to
    # continue the original task after an interruption
else:
    event_did_not_happen_before_completion()

# some methods provide different error conditions via flags

try:
    # check_inventory waits a bit for the hand slot to get updated,
    # and checks that the item count is one fewer, implying placement success
    bot.place_block_against(xyz, face="top", check_inventory=True, look=True)
except PlacementFailed as e:
    handle_failure(e)
else:
    handle_success()

try:
    bot.walk_to(location1, fail_on_collision=True)
    bot.walk_to(location2, fail_when_stuck=True)
    bot.walk_to(location3, timeout_ticks=200)
    # or
    with timeout_ticks(200):
        bot.walk_to(location3)
except MovementCollision as e:
    handle_collision()
except MovementStuck as e:
    handle_stuck()
except Timeout as e:
    handle_timeout()
else:
    handle_success()
