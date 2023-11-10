# This script contains the prologue scene of Act 1

# Declare the characters for this scene.
define jun = Character("Jun", color="#00aaff")
define aditi = Character("Aditi", color="#ff00aa")

# Start the prologue
label scene_prologue:

    # Start playing the music
    play music "audio/Flood_of_Death.mp3"
    
    # Setting the scene with the siblings on the bike
    image bg splash_bike_2 = "images/assets/cg/splash_bike_2.png"

    scene splash_bike_2

    # Aditi's dialogue
    aditi "Jun! Don’t go so fast! You’re going to get us both killed!"
    
    # Jun's response
    jun "Yeah yeah yeah."

    # Jun's inner thoughts
    "This sister of mine…"

    # Aditi's frantic thoughts
    aditi "Oh gods. I’m gonna die. I’m gonna die. I’m gonna die."

    # Switching to the second CG
    image bg prologue_bike = "images/assets/cg/prologue_bike.png"

    scene prologue_bike

    # Jun's cheery response
    jun "I promise we’ll only die after we reach the Gate."

    # Jun's inner thoughts
    "If we succeed in closing the gate…"
    "The monsters won’t be able to come to our world anymore."
    "It will all be over."
    "Will we still be alive to see that…? I wonder."
    "We have to be. We really can’t die yet. We’ve still got so much to do."
    "But I guess I should start from the beginning, huh? How would you know why we’re here?"
    "We-ell, it all began just today morning. I guess I have had a {i}very{/i} productive day."

    stop music fadeout 1.0


    # Return to main script
    return
