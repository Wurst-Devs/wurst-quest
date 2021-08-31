import logging
import time

from .core import Game, Autoplay


def main():
    logging.basicConfig(
        format="[%(asctime)s][%(levelname)s][%(module)s] %(message)s",
        level=logging.DEBUG,
    )

    game = Game()
    game.init()

    autoplay = Autoplay()

    state = game.new_game()

    while True:
        action = autoplay.next_action(state)

        logging.info(f"{state.status}...")
        logging.debug(
            f"{state.location.name} / {action.type.name}\n\t{state.player}\n\t{state.monster}"
        )
        time.sleep(state.duration)

        state = game.compute(state, action)


if __name__ == "__main__":
    main()
