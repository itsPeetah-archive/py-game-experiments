def editor_help():
    help = '''
    COMMANDS:

        escape -> quit
        v -> v mode
        w -> single/continued wall mode
        a -> set start mode
        t -> train mode

    WALL MODE:
        left click -> build wall
        return -> close wall (at mouse position)
        s -> save walls to walls.txt
        l -> load walls from walls.txt
        c -> clear walls
    SET START MODE:
        left click -> set spawnpoint
        right click -> set direction
    '''
    print(help)

def game_help():
    help = '''
    COMMANDS:
        - ctrl + l = load map
        - ctrl + q = quit game
        - ctrl + i = start from zero
        - ctrl + s = save current generation (thought process)
        - ctrl + t = load saved generation (thought process)
    '''
    print(help)
