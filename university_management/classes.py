
class Classes:
    def __init__(self) -> None:
        self.list_of_classes: list[str] = ["Class A", "Class B", "Class C"]

    def show_classes(self) -> None:
        print(f"\n{'-'*10} Classes Info {'-'*10}")
        print(f"Available Classes: {', '.join(self.list_of_classes)}")
        print(f"{'-'*35}\n")
