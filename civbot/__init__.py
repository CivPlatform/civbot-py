def TODO(): raise Error("Not implemented")

class Bot:
    game_address: str
    name: str
    uuid: str

    def __init__(self, game_address: str):
        TODO()

    players_online: PlayersOnline
    health: float
    food: float

    def respawn(self):
        TODO()

    def chat(self, msg: str):
        TODO()

    def wait_ticks(self, ticks: int):
        TODO()

    feet: Vec3
    eyes: Vec3
    look: Look

    def look_at(self, location: XYZ):
        TODO()

    def look_horizontal(self, location: XYZ):
        TODO()

    def walk_to(self, location: XYZ, arrival_precision=0.01):
        TODO()

    def start_walking_towards(self, location: XYZ):
        TODO()

    def stop_walking(self):
        TODO()

    def start_jump(self):
        TODO()

    def jump_by_height(self, height: int):
        TODO()

    def leave_bed(self):
        TODO()

    def activate_block(self, location: XYZ, face: BlockFace, look=True):
        TODO()

    def place_block_against(self, location: XYZ, face: BlockFace, look=True, check_inventory=True):
        TODO()

    hotbar: list[Slot]
    main_hand: Slot
    off_hand: Slot

    def open_inventory(self) -> OpenWindow:
        """
        use like this:

            with open_block_window(chest_location, "top") as win:
                win.deposit(64, "dirt")
        """
        TODO()

    def open_block_window(self, location: XYZ, face: BlockFace, look=True) -> OpenWindow:
        TODO()

    def hold_item(self, item: ItemSpec) -> int:
        TODO()

    def start_using_item(self, hand="main"):
        TODO()

    def stop_using_item(self):
        TODO()

    digging_location: Vec3

    def dig(self, location: XYZ, face: BlockFace, ticks: int, look=True):
        TODO()

    def start_digging(self, location: XYZ, face: BlockFace, look=True):
        TODO()

    def finish_digging(self):
        TODO()

    def cancel_digging(self):
        TODO()

# TODO Vec3 is always a full class with utility methods
# TODO XYZ can be an (x,y,z) tuple, or a Vec3, or ...

class Window:
    slots: list[Slot]

    def count(self, item: ItemSpec) -> int:
        TODO()

    def deposit(self, count: number | "all", item: ItemSpec) -> int:
        TODO()

    def withdraw(self, count: number | "all", item: ItemSpec) -> int:
        TODO()

class PlayersOnline:
    all: list[PlayerInfo]

    def by_uuid(self, uuid: str) -> list[PlayerInfo]:
        TODO()

    def by_name(self, name: str) -> list[PlayerInfo]:
        TODO()

class PlayerInfo:
    uuid: str
    name: str
    online_since: int

class OpenWindow:
    def __init__(self):
        self.win = wait_event("window_open")
        add_event_handler("window_closed", self._on_close)

    def __enter__(self) -> Window:
        return self.win

    def __exit__(self, err_type, err_val, err_trace) -> bool:
        remove_event_handler("window_closed", self._on_close)

    def _on_close(self):
        win.throw_closed_error()
