# This script contains the Scene 2 of Act 2

# Reusing the characters from the previous scene.
define jun = Character("Jun", color="#00aaff")
define aditi = Character("Aditi", color="#ff00aa")

# Start the scene 2
label scene_2:

    # Setting the scene with the siblings facing each other, tension evident.
    image bg living_room_tense = "images/assets/bg/scene_1_both_sit_bg_1.png" 

    scene bg living_room_tense

    show jun sad_couch

    show aditi shiftingeyes

    # Jun's inner thoughts
    "It’s here. Our death is here."
    "Goodbye, world. I lived a…life. Not a long life, or an interesting one, but it was a life."

    image aditi determined = "images/assets/character_sprites/aditi/scene_2/scene_2_aditi_sit_determined.png"

    # Aditi determined
    show aditi determined
    aditi "It’s here, huh?"

    image jun blank = "images/assets/character_sprites/jun/scene_2/scene_2_jun_blank.png"

    # Jun blank
    show jun blank
    jun "Our deaths? Yeah…"


    # Aditi has a realization
    aditi "No. I just realized something."
    "Huh?"
    aditi "Exactly three weeks ago, Akshara called me. She seemed…like she was exhausted. I thought it was just those in-laws of hers. But now I think it might have been something else."

    # Jun's inner thoughts
    "These sisters and their talks that I am not allowed to butt into. It’s so annoying being the youngest."

    show jun sweatdrop

    jun "Yeah? And I suppose that’s when she told you about the seal."

    image aditi careless = "images/assets/character_sprites/aditi/scene_2/scene_2_aditi_sit_careless.png"

    # Aditi careless
    show aditi careless
    aditi "She never actually gave me specifics, you know… just explained her work a bit…Anyway!"

    show aditi frantic

    # Aditi frantic
    aditi "She said that she was worried she’d be pulled ‘beyond’. I thought she was just being metaphorical, but now I think she’s really beyond the Gates!"

    show jun blank 

    # Jun's inner thoughts
    "…what’s a metaphor?"
    "Wait. WAIT!"
    "This sister of mine…"
    "They never tell me anything."

    image aditi pity = "images/assets/character_sprites/aditi/scene_2/scene_2_aditi_sit_pity.png"

    show aditi pity

    # Aditi explains metaphor
    aditi "Jun-Jun, a metaphor is a figure of speech that compares two seemingly unrelated things. Now, back on topic. ‘Time is money’, you know?"

    # Aditi shows a map
    image bg map_with_red_spots = "images/assets/cg/scene_2/scene_2_map_ cg.png" # Replace with actual image path.

    scene bg map_with_red_spots

    aditi "And did you notice? The Gates started east of here, but they’ve slowly been zeroing in on us. Look at this!"

    scene bg living_room_tense

    show jun blank

    show aditi determined

    # Jun blank
    jun "I thought they just hated Indeka or something…"

    image aditi fiery = "images/assets/character_sprites/aditi/scene_2/scene_2_aditi_sit_fiery.png"

    show aditi fiery

    aditi "Jun-Jun!"

    show jun sad_couch

    # Jun determined
    jun "Okay, Okay. What do we do now?"
    "We can't just sit and wait, but it's too risky out there."


    # Aditi fiery
    aditi "Jun! We have to try, for Akshara. You know what they are saying about her!"

    image jun worried = "images/assets/character_sprites/jun/scene_2/scene_2_jun_couch_worried.png"

    # Jun worried
    show jun worried 

    jun "What would we even be able to do?"

    # Aditi determined

    show aditi determined 

    aditi "We can close the Gates, starting with the main one."

    show jun blank

    # Jun blank
    jun "What? Wouldn’t that…just lock sister Akshara away?"

    # Aditi has a plan
    aditi "Akshara’s words were a clue. She gave me clues to close the Gates."
    aditi "That means, closing the Gates might pull her back to our world. If she was pulled beyond through a Gate…she can be pulled back if we break the connection to the monster’s world."

    # Aditi thinking
    show aditi shiftingeyes
    aditi "Come to think of it, don’t random things always come out of the Gates? Table fans, refrigerators, telephone poles…It’s connecting…"

    show jun calm

    # Jun's inner thoughts
    "Aditi goes on muttering. I don’t understand a word of it."
    "But I do understand one thing."
    "I need to…"

    # Soft, contemplative music.
    # play music "assets/music/soft_contemplative.mp3" # Replace with the actual path to your music.

    # Jun's choices
    menu:
        "Go out and close the Gate":
            jun "Okay. I trust you, sister. What do we need to do?"
            call scene_3_1
            # The game will continue in scene 3_1.

        "Stay put":
            jun "Maybe it's safer if we just stay here."
            # The game will branch here based on the choice.

    # Return to main script
    return
