import logging

from .models import Action, State
from .factories import MonsterFactory
from .content import Content
from .enums import Location, ActionType


class Game:
    ENCOUNTER_CHANCE = 90
    FLEE_CHANCE = 90
    TIME_QUICK = 1
    TIME_NORMAL = 3
    TIME_LONG = 10

    def __init__(self) -> None:
        pass

    @property
    def content(self) -> Content:
        return Content.get_instance()

    def init(self) -> None:
        logging.info("loading data...")
        self.content.init()

        # TODO

    def new_game(self) -> State:
        logging.info("new game:")
        return State(
            location=Location.CITY,
            duration=Game.TIME_LONG,
            status="Starting new adventure",
        )

    def compute(self, state: State, action: Action) -> State:
        state = state.clone()
        if state.location == Location.CITY:
            return self._compute_city(state, action)
        elif state.location == Location.OUTSIDE:
            return self._compute_outside(state, action)
        elif state.location == Location.BATTLE:
            return self._compute_battle(state, action)

    def _compute_city(self, state: State, action: Action) -> State:
        if state.player.hp < state.player.max_hp:
            state.player.hp = state.player.max_hp
            state.update(
                location=Location.CITY,
                duration=Game.TIME_NORMAL,
                status="Healing",
                monster=None,
            )
        elif action.type == ActionType.BUY:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_LONG,
                status="Buying things",
                monster=None,
            )
            # TODO
        elif action.type == ActionType.LEAVE:
            state.update(
                location=Location.OUTSIDE,
                duration=Game.TIME_NORMAL,
                status="Leaving the city",
                monster=None,
            )
        else:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_QUICK,
                status="Waiting",
                monster=None,
            )
        return state

    def _compute_outside(self, state: State, action: Action) -> State:
        if action.type == ActionType.RETREAT:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_NORMAL,
                status="Going back to the city",
                monster=None,
            )
        elif action.type == ActionType.SEARCH:
            if state.random.randrange(0, 99) < Game.ENCOUNTER_CHANCE:
                monster = MonsterFactory(state.random)
                state.update(
                    location=Location.BATTLE,
                    duration=Game.TIME_QUICK,
                    status=f"A wild {monster.name} appears",
                    monster=monster,
                )
            else:
                state.update(
                    location=Location.OUTSIDE,
                    duration=Game.TIME_NORMAL,
                    status=f"Nothing found while searching",
                    monster=None,
                )
        else:
            state.update(
                location=Location.OUTSIDE,
                duration=Game.TIME_QUICK,
                status="Waiting",
                monster=None,
            )
        return state

    def _compute_battle(self, state: State, action: Action) -> State:
        if state.monster.hp <= 0:
            if action == ActionType.SEARCH:
                loot = MonsterFactory(state.random).generate_loot(state.monster)
                if loot[0] is not None:
                    state.player.inventory += [loot]
                    status_text = "Found {loot[0]}"
                else:
                    status_text = "Found nothing"
                state.update(
                    location=Location.OUTSIDE,
                    duration=Game.TIME_NORMAL,
                    status=status_text,
                    monster=None,
                )
            else:
                state.player.experience += state.monster.experience_gain
                state.update(
                    location=Location.OUTSIDE,
                    duration=Game.TIME_NORMAL,
                    status=f"Defeated {state.monster.name}, searching the body",
                    monster=None,
                )
        elif state.player.hp <= 0:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_LONG,
                status=f"Defeated by {state.monster.name}, going back to city",
                monster=None,
            )
        else:
            # TODO equippment
            player_attack = 1
            monster_attack = state.monster.attack
            # TODO handle first hit
            state.monster.hp -= player_attack
            status_text = f"{state.monster.name} takes {player_attack}"
            if state.monster.hp > 0:
                state.player.hp -= monster_attack
                status_text = f" and retaliates with {monster_attack}"
            else:
                status_text = f" and dies"
            if action == ActionType.FLEE:
                if state.random.randrange(0, 99) < Game.FLEE_CHANCE:
                    state.update(
                        location=Location.OUTSIDE,
                        duration=Game.TIME_NORMAL,
                        status=f"Fleeing combat",
                        monster=None,
                    )
                    return state
                else:
                    state.monster.hp += player_attack  # cancel player attack
                    status_text = (
                        f"Could not flee combat, took {monster_attack} while trying"
                    )
            state.update(
                location=Location.BATTLE,
                duration=Game.TIME_QUICK,
                status=status_text,
            )
        return state
