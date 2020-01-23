import typing
import uuid
from dataclasses import field

from pydantic import validator
from pydantic.dataclasses import dataclass
from pypika import Table


def uuid_factory() -> str:
    return str(uuid.uuid4())


@dataclass
class Base:
    @staticmethod
    def table_name() -> str:
        raise NotImplementedError

    @staticmethod
    def table() -> Table:
        raise NotImplementedError


@dataclass
class Card(Base):
    name: str

    id: int = None
    uuid: str = field(default_factory=uuid_factory)


@dataclass
class Character(Base):
    name: str

    id: int = None
    uuid: str = None


@dataclass
class Enemy(Base):
    name: str

    id: int = None
    uuid: str = None


@dataclass
class Relic(Base):
    @staticmethod
    def table_name() -> str:
        return 'relics'

    @staticmethod
    def table() -> Table:
        return Table(Relic.table_name())

    name: str
    flavor: str

    id: int = None
    uuid: str = field(default_factory=uuid_factory)


    @validator('name')
    def name_valid(cls, v):
        return v


@dataclass
class RunRelic(Base):
    card_id: int
    relic_id: int


@dataclass
class RunCard(Base):
    card_id: int
    run_id: int


@dataclass
class Run(Base):
    build_version: str
    timestamp: int
    local_time: str

    ascension_level: int
    victorious: bool
    gold: int
    duration: int
    score: int

    character: Character

    is_ascension: bool
    is_beta: bool
    is_seeded: bool
    is_daily: bool
    is_endless: bool
    is_prod: bool
    is_trial: bool

    neow_bonus: str
    neow_cost: str

    seed: str
    seed_timestamp: int
    seeded: bool


@dataclass
class Event(Base):
    floor_id: int
    name: str

    heal: int
    damage: int

    max_hp_gain: int
    max_hp_loss: int

    gold_gain: int
    gold_loss: int

    choice: str

    relics_obtained: str
    cards_removed: str
    cards_upgraded: str

    id: int = None
    uuid: str = None


@dataclass
class Purchase(Base):
    floor_id: int
    item: str # RELIC OR CARD


@dataclass
class Purge(Base):
    floor_id: int
    card: Card


@dataclass
class FloorRelic(Base):
    floor_id: int
    relic_id: int


@dataclass
class Floor(Base):
    run_id: int
    level: int

    field: str

    campfire_action: str
    campfire_data: str

    picked: str
    not_picked: typing.Sequence[str]

    max_hp: int
    hp: int
    gold: int

    enemies: Enemy
    damage: int
    turns: int

    event: Event

    relics: typing.Sequence[Relic]

    id: int = None
    uuid: str = None
