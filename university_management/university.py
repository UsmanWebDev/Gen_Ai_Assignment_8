
class University:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def show_info(self) -> None:
        print(f"\n{'-'*10} University Info {'-'*10}")
        print(f"University Name: {self.name}")
        print(f"{'-'*35}\n")
