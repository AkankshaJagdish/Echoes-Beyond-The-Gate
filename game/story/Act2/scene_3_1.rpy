# This script contains the Scene 3_1 of Act 2

# Assuming the characters have already been defined in the previous scenes.
# define jun = Character("Jun", color="#00aaff")
# define aditi = Character("Aditi", color="#ff00aa")

# Start the scene 3_1
label scene_3_1:
    image bg living_room_seated = "images/assets/bg/scene_1_both_sit_bg_1.png" 

    scene bg living_room_seated

    show jun calm

    image aditi cheery = "images/assets/character_sprites/aditi/scene_3_1/scene_3_1_aditi_sit_cheery.png"

    # Aditi cheery
    show aditi cheery
    aditi "Little brother! I love you so much! You are so cute! I knew you’d agree!"

    image jun cool_2 = "images/assets/character_sprites/jun/scene_1/scene_1_jun_couch_cool_2.png"

    # Jun coolly
    show jun cool_2
    jun "Sister, please shut up."

    # Aditi working on the seal
    
    aditi "I’ll try to make the seal again now!"

    # Aditi worried
    show aditi sit_worried
    aditi "Although I’m not sure if I {i}can{/i} make it again…"

    # Jun encouraging
    show jun sweatdrop
    jun "You can do it! If you can’t, we’re all dead, so you can do it!"

    image aditi sit_annoyed = "images/assets/character_sprites/aditi/scene_3_1/scene_3_1_aditi_sit_annoyed.png"

    # Aditi annoyed
    show aditi sit_annoyed
    aditi "Jun-Jun!"

    scene bg living_room_only_jun
    show jun jun_couch

    # Jun's inner thoughts and time passage
    "My dearest sister troops away."
    with Pause(10) # 30 second pause in game

    image bg living_room_with_seal = "images/assets/bg/scene_3_1_aditi_jun_seal.png"

    scene bg living_room_with_seal

    image jun calm_2 = "images/assets/character_sprites/jun/scene_3_1/scene_3_1_jun_calm_2.png"

    show jun calm_2

    image aditi seal_worried = "images/assets/character_sprites/aditi/scene_3_1/scene_3_1_aditi_worried.png"

    show aditi seal_worried

    # Jun's inner thoughts after time skip
    "Three hours later, my sister returns. She holds a piece of paper in her hands, fiddling with it."
    

    # Aditi worried with the seal
    aditi "Okay..."
    aditi "So I made the seal..."

    # Aditi expressing doubt
    aditi "But do I have any idea if it works? No. Can I test it? Not without risking my life."

    image aditi seal_sad = "images/assets/character_sprites/aditi/scene_3_1/scene_3_1_aditi_sad.png"

    # Aditi sad
    show aditi seal_sad
    aditi "We’re so done for if it doesn’t work..."

    image jun sweatdrop_2 = "images/assets/character_sprites/jun/scene_3_1/scene_3_1_jun_sweatdrop_2.png"

    show jun sweatdrop_2

    # Jun's inner monologue
    "There she goes again."
    "Sister has made many projects, and succeeded at most of them."
    "I agree that this is a project that is, well, world changing. But she’s a genius, y’know?"
    "She’s probably done it right."

    image seal_sparks_1 = "images/assets/character_sprites/aditi/scene_3_1/scene_3_1_seal_sparks.png"

    # Aditi channels power
    show aditi seal_worried
    "My sister puts her palm on the paper and channels her power through it."

    show seal_sparks_1

    # Visual effects for the power
    # play sound sparks_flying

    # Aditi worried
    show aditi seal_sad
    aditi "It's harder than it looks. And I don’t know if it works…"

    hide image seal_sparks_1

    show jun calm_2

    # Jun offers help
    jun "Here. Let me help."

    # Jun's inner thoughts
    "My illusions can actually become real if left on for too long. If it’s a small illusion, I can make it happen a but more quickly."
    "I… I think I can make a Gate. Or a simulation of one. A small simulation of one."

    show jun sad

    # Jun focusing
    "Okay… focus on what you heard in the news…"

    # Illusions of rifts
    # play sound rifts_start
    "Illusions of rifts appear around the kitchen."

    # Aditi grateful
    show aditi seal_worried
    aditi "You really are the best, little brother."

    image jun embarrassed_2 = "images/assets/character_sprites/jun/scene_3_1/scene_3_1_jun_embarrassed_2.png"

    # Jun coolly
    show jun embarrassed_2
    jun "Again with the ‘little’… Get started already."

    # Start the mini-game to open and close rifts
    # Note: Actual mini-game code should be implemented here based on the game design.
    # This is a placeholder for the mini-game call.
    # call play_minigame

    # Sound effects and music
    # play sound rifts_closing
    # play music encouraging_music

    image jun surprised_2 = "images/assets/character_sprites/jun/scene_3_1/scene_3_1_jun_surprised.png"

    # Jun's approval
    show jun surprised_2
    jun "Well, that was pretty good!"

    image aditi seal_calming = "images/assets/character_sprites/aditi/scene_3_1/scene_3_1_aditi_calming.png"


    # Aditi calming
    show aditi seal_calming
    aditi "I guess.. I feel a bit more confident now."

    # End of scene 3_1
    return
