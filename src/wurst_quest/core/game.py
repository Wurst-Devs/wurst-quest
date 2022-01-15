import logging

from .models import Action, State
from .factories import MonsterFactory, PlayerFactory
from .content import Content
from .enums import Location, ActionType, PlayerGear


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

    def new_game(self) -> State:
        logging.info("new game:")
        state = State(
            location=Location.CITY,
            duration=Game.TIME_NORMAL,
            status="Starting new adventure",
        )
        state.player = PlayerFactory(state.random).new_player()
        return state

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
                locked=False,
            )
        elif action.type == ActionType.BUY:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_LONG,
                status="Buying things",
                monster=None,
                locked=False,
            )
            # TODO
        elif action.type == ActionType.LEAVE:
            state.update(
                location=Location.OUTSIDE,
                duration=Game.TIME_NORMAL,
                status="Leaving the city",
                monster=None,
                locked=False,
            )
        else:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_QUICK,
                status="Waiting",
                monster=None,
                locked=False,
            )
        return state

    def _compute_outside(self, state: State, action: Action) -> State:
        can_level_up = PlayerFactory(state.random).can_level_up(state.player)
        if can_level_up and state.locked:
            state.player = PlayerFactory(state.random).level_up(state.player)
            state.update(
                location=Location.OUTSIDE,
                duration=Game.TIME_QUICK,
                status="Leveled up",
                monster=None,
                locked=False,
            )
        elif action.type == ActionType.RETREAT:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_NORMAL,
                status="Going back to the city",
                monster=None,
                locked=False,
            )
        elif action.type == ActionType.SEARCH:
            if state.random.randrange(0, 99) < Game.ENCOUNTER_CHANCE:
                monster = MonsterFactory(state.random).generate_monster(
                    state.player.level
                )
                state.update(
                    location=Location.BATTLE,
                    duration=Game.TIME_QUICK,
                    status=f"A wild {monster.name} appears",
                    monster=monster,
                    locked=False,
                )
            else:
                state.update(
                    location=Location.OUTSIDE,
                    duration=Game.TIME_NORMAL,
                    status=f"Nothing found while searching",
                    monster=None,
                    locked=False,
                )
        else:
            state.update(
                location=Location.OUTSIDE,
                duration=Game.TIME_QUICK,
                status="Waiting",
                monster=None,
                locked=False,
            )
        return state

    def _compute_battle(self, state: State, action: Action) -> State:
        if state.monster.hp <= 0:
            if not state.locked:
                state.player.experience += state.monster.experience_gain
                state.update(
                    location=Location.BATTLE,
                    duration=Game.TIME_NORMAL,
                    status=f"Defeated {state.monster.name}, searching body",
                    locked=True,
                )
            else:
                loot = MonsterFactory(state.random).generate_loot(state.monster)
                if loot is not None:
                    state.player.inventory += [loot]
                    status_text = f"Found {loot.name}, searching for another monster"
                else:
                    status_text = "Found nothing, searching for another monster"
                can_level_up = PlayerFactory(state.random).can_level_up(state.player)
                state.update(
                    location=Location.OUTSIDE,
                    duration=Game.TIME_NORMAL,
                    status=status_text,
                    monster=None,
                    locked=can_level_up,
                )
        elif state.player.hp <= 0:
            state.update(
                location=Location.CITY,
                duration=Game.TIME_LONG,
                status=f"Defeated by {state.monster.name}, going back to city",
                monster=None,
                locked=False,
            )
        else:
            # TODO equippment
            player_attack = state.player.equipped[PlayerGear.WEAPON].value
            monster_attack = state.monster.attack
            # TODO handle first hit
            state.monster.hp -= player_attack
            status_text = f"{state.monster.name} takes {player_attack}"
            if state.monster.hp > 0:
                state.player.hp -= monster_attack
                status_text += f" and retaliates with {monster_attack}"
            else:
                status_text += f" and dies"
            if action.type == ActionType.FLEE:
                if state.random.randrange(0, 99) < Game.FLEE_CHANCE:
                    state.update(
                        location=Location.OUTSIDE,
                        duration=Game.TIME_NORMAL,
                        status=f"Fleeing combat",
                        monster=None,
                        locked=False,
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
                locked=False,
            )
        return state
