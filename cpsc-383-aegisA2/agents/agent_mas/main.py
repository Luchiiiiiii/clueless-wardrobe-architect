from aegis_game.stub import *

# ============================================================
# CPSC 383 — Assignment 2
# Date: 
# Course: CPSC 383
# Semester: Fall 2026
# Tutorial: 
#
# Group members (Sections):
#   P1 — Ishmam, Muhtasim         (Section A — Perception)
#   P2 — Chakrabarty, Susmita     (Section B — Pathfinding)
#   P3 — Anika, Nusrat            (Section C — Messaging)
#   P4 — Ani, Oluchukwu           (Section D — Strategy + Integration)
#
# Citations:
#   A* pathfinding adapted from the A1 submission of [group member name]
#   (file: [A1 main.py], [date submitted]).
#
# GenAI usage:
#   [Describe tool, e.g. "Claude/ChatGPT was used for design discussion
#   and code review. All code was written and verified by the group.
#   No code was pasted directly from AI output without review."]
# ============================================================



# ============================================================
# SECTION A — PERCEPTION & MAP MODEL        Owner: P1
# ============================================================
known_map: dict = {}
visited: set = set()
survivor_locs: set = set()


def update_known_map() -> None:
    """P1 will implement. Safe default: no-op."""
    pass


def known_cost(loc) -> int:
    """P1 will implement. Safe default: cost 1."""
    return 1


def is_killer(loc) -> bool:
    """P1 will implement. Safe default: not killer."""
    return False


def is_charger(loc) -> bool:
    """P1 will implement. Safe default: not charger."""
    return False


def stack_at(loc):
    """P1 will implement. Safe default: unknown."""
    return None


def rubble_required_agents(loc) -> int:
    """P1 will implement. Safe default: no rubble."""
    return 0


def rubble_energy(loc) -> int:
    """P1 will implement. Safe default: no rubble."""
    return 0


def adjacent_to_goal(loc) -> bool:
    """P1 will implement. Safe default: false."""
    return False


def refresh_survivors() -> set:
    """P1 will implement. Safe default: empty."""
    return set()


# ============================================================
# SECTION B — PATHFINDING                    Owner: P2
# ============================================================
def plan_path(start, goal):
    """P2 will implement. Safe default: no path."""
    return None


def path_cost(path) -> int:
    """P2 will implement. Safe default: 0."""
    return 0


def step_toward(path):
    """P2 will implement. Safe default: hold."""
    return Direction.CENTER


def plan_path_with_charging(start, goal, energy):
    """P2 will implement (Stage 3). Safe default: fall back to plan_path."""
    return plan_path(start, goal)


# ============================================================
# SECTION C — MESSAGING & COORDINATION       Owner: P3
# ============================================================
my_target = None
claimed_targets: dict = {}


def pack(msg_type: str, *args) -> str:
    """P3 will implement. Safe default: naive join."""
    return "|".join([msg_type] + [str(a) for a in args])


def process_incoming() -> None:
    """P3 will implement. Safe default: no-op."""
    pass


def claim_target():
    """P3 will implement. Safe default: None."""
    return None


def request_dig_partner(loc) -> None:
    """P3 will implement. Safe default: no-op."""
    pass


def on_dig_pos(loc) -> None:
    """P3 will implement. Safe default: no-op."""
    pass


def handshake_state() -> str:
    """P3 will implement. Safe default: idle."""
    return "NONE"


# ============================================================
# SECTION D — STRATEGY & think()             Owner: P4
# ============================================================
# 
def think() -> None:
    """Do not remove this function, it must always be defined."""
    log("Thinking")

    # On the first round, send a request for surrounding information
    # by moving to the center (not moving). This will help initiate pathfinding.
    if get_round_number() == 1:
        move(Direction.CENTER)
        send_message("hello world", [])  # Broadcast to all teammates
        return

    # On subsequent rounds, read and log all received messages.
    messages = read_messages()
    log(messages)

    # Fetch the cell at the agent's current location.
    # If you want to check a different location, use `on_map(loc)` first
    # to ensure it's within the world bounds. The agent's own location is always valid.
    cell = get_cell_info_at(get_location())

    # Get the top layer at the agent's current location.
    # If a survivor is present, save it and end the turn.
    top_layer = cell.top_layer
    if isinstance(top_layer, Survivor):
        save()
        return

    # Default action: Move the agent north if no other specific conditions are met.
    move(Direction.NORTH)
