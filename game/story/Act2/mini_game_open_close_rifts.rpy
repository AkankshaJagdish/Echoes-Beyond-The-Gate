init python:

    import random
    from datetime import datetime, timedelta

    class Gate:
        def __init__(self, xpos, ypos):
            self.xpos = xpos
            self.ypos = ypos

    class Spark:
        def __init__(self, xpos, ypos):
            self.xpos = xpos
            self.ypos = ypos

    gates = []
    sparks = []
    spark_spawn_rate = 1.0  # Spark spawn every 1 second
    spark_timer = datetime.now()  # Initialize as a datetime object

    def minigame_create_gate():
        mouse_x, mouse_y = renpy.get_mouse_pos()
        gates.append(Gate(mouse_x, mouse_y))
        renpy.restart_interaction()  # Restart the interaction to update the screen.

    def minigame_spawn_spark():
        global spark_spawn_rate, sparks, gates
        if gates:
            gate = random.choice(gates)
            sparks.append(Spark(gate.xpos, gate.ypos))
            gates.remove(gate)
            # Increase the difficulty by making sparks appear faster
            spark_spawn_rate = max(0.1, spark_spawn_rate * 0.70)
            print("Spawned spark at ({}, {}). New rate: {}".format(gate.xpos, gate.ypos, spark_spawn_rate))  # Debug print
            renpy.restart_interaction()  # Restart to show the new spark
        else:
            # If there are no gates left, jump to end_game
            renpy.jump("end_game")

    def periodically_create_sparks():
        global spark_timer, spark_spawn_rate
        current_time = datetime.now()
        if current_time - spark_timer >= timedelta(seconds=spark_spawn_rate):
            print("Time to spawn a new spark.")  # Debug print
            spark_timer = current_time
            minigame_spawn_spark()



screen minigame_gates():

    # This imagemap allows the player to click anywhere to create a gate.
    imagemap:
        ground ""
        idle "images/assets/minigame/background.png"
        hover "images/assets/minigame/background.png"
        hotspot (0, 0, 1280, 720) action minigame_create_gate

    # This displays all the gates that are currently on the screen.
    for gate in gates:
        add "images/assets/minigame/gate.png" xpos gate.xpos ypos gate.ypos

    # This displays all the sparks that are currently on the screen.
    for spark in sparks:
        add "images/assets/minigame/sparks.png" xpos spark.xpos ypos spark.ypos

    # Show the character sprite bouncing at the side
    add "images/assets/minigame/aditi.png" xpos 50 ypos 50

    # Show the player character on the opposite side
    add "images/assets/minigame/jun.png" xpos 1130 ypos 650  # Adjust xpos to fit the screen

    timer 0.1 action Function(periodically_create_sparks)


label play_minigame:
    # Call the minigame screen and wait until it finishes.
    call screen minigame_gates

label end_game:
    # The game ends here, you can transition to another scene or display a message.
    # Add any cleanup code if necessary before ending the minigame.
    return
