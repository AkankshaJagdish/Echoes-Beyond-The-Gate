# This is the main script for the game.

# The game starts here.

label start:

    image splash = "assets/cg/splash_bike_1.png"

    # Show the splash screen
    scene splash
    with Pause(2.0) # Pausing for 2 seconds on the splash screen

    # Start the prologue scene
    call scene_prologue

    # This ends the game.
    return
