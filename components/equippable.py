from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        regen_bonus: int = 0,
        power_bonus: int = 0,
        defense_bonus: int = 0,
    ):
        self.equipment_type = equipment_type

        self.regen_bonus = regen_bonus
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus


class Shiv(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)


class LeadPipe(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=5, regen_bonus=1)

class StaplerNunchucks(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, regen_bonus=-1, power_bonus=10, defense_bonus=2)


class BlueJumpSuit(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=2)


class CosplayArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=3)

class MilGradeFatigues(Equippable):
    def __init__(self):
        super().__init__(equipment_type=EquipmentType.ARMOR, regen_bonus=1, power_bonus=1, defense_bonus=5)