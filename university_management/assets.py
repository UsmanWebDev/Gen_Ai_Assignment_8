
from .university import University

class Assets(University):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.list_of_bus: list[str] = []
        self.list_of_table: list[str] = []
        self.list_of_room_cooler: list[str] = []
        self.list_of_AC: list[str] = []
        self.list_of_computer: list[str] = []

    def add_bus(self, bus: str) -> None:
        self.list_of_bus.append(bus)

    def add_table(self, table: str) -> None:
        self.list_of_table.append(table)

    def add_room_cooler(self, room_cooler: str) -> None:
        self.list_of_room_cooler.append(room_cooler)

    def add_AC(self, AC: str) -> None:
        self.list_of_AC.append(AC)

    def add_computer(self, computer: str) -> None:
        self.list_of_computer.append(computer)

    def show_assets(self) -> None:
        print(f"\n{'-'*10} University Assets {'-'*10}")
        print(f"Buses: {', '.join(self.list_of_bus)}")
        print(f"Tables: {', '.join(self.list_of_table)}")
        print(f"Room Coolers: {', '.join(self.list_of_room_cooler)}")
        print(f"ACs: {', '.join(self.list_of_AC)}")
        print(f"Computers: {', '.join(self.list_of_computer)}")
        print(f"{'-'*35}\n")
