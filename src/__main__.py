import logging
import time

from core import Game, Autoplay

if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s][%(levelname)s][%(module)s] %(message)s",
        level=logging.INFO,




    )

    game = Game()
    game.
    init()

    autoplay = Autoplay()

    state = game.new_game()

    while True:


          logging.info(f"{state.status}...")
        time.sleep(state.duration)

        action = autoplay.next_action(state)

        state = game.compute(state, action)
