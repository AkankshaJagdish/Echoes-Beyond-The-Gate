# This script contains the Scene 1 of Act 1

# Declare the characters for this scene.
define jun = Character("Jun", color="#00aaff")
define aditi = Character("Aditi", color="#ff00aa")
define broadcast = Character("Broadcast")

# Start the scene 1
label scene_1:

    # Setting the scene in the dimly lit living room
    image bg living_room_only_jun = "images/assets/bg/scene_1_livingroom_dim_only_jun.png" # Please replace with the actual path when you add the image.

    scene bg living_room_only_jun
    
    # play music "assets/music/tense_bg_music.mp3" # Replace with the actual path to your music.

    image jun jun_couch = "images/assets/character_sprites/jun/scene_1_jun_couch.png"

    show jun jun_couch
    
    # Jun's narration
    "Hello. I’m Jun. Or well, Arjuna, but my sisters call me Jun. Cause well, I’m Arjuna and I was born in June."
    "Also, I’m an Esper. I can cast illusions. That’s why I got an invite to the Indekan Defense Academy a little early. I was, like, 16. I was rather pleased with it. Getting out of school early! Yeah!"
    "Until now, that is. I was on leave - because of course I was - and these Gates appeared that spewed monsters all over the place. Now all I have to defend myself are these illusions that people can literally walk through."
    "I’m so dead."
    "My team members contacted me and told me to stay put. This entire city is on lock-down."
    "Wait. I should be glad I was on leave. Because…"

    image bg living_room_aditi_enters = "images/assets/bg/scene_1_livingroom_dim_aditi_enters.png" # Please replace with the actual path when you add the image.

    image aditi stand_worried = "images/assets/character_sprites/aditi/scene_1_aditi_stand_worried.png"

    scene bg scene_1_livingroom_dim_aditi_enters

    show aditi stand_worried

    # Aditi appears in the doorway
    aditi "Jun! David told me there’s a monster in the neighborhood. What do we do?"

    "My sister would definitely be in trouble without me."

    image jun coolly = "images/assets/character_sprites/jun/scene_1_jun_couch_cool.png"
    
    show jun coolly

    jun "‘David’? You’re talking to a boy?"

    image bg jun_aditi = "images/assets/bg/scene_1_livingroom_dim_jun_aditi.png"

    scene bg jun_aditi

    image aditi annoyed = "images/assets/character_sprites/aditi/scene_1_aditi_stand_annoyed.png"

    show aditi annoyed

    show jun coolly

    aditi "Jun! You - You little -"
    "It’s kind of fun annoying her like this."

    image jun calm = "images/assets/character_sprites/jun/scene_1_jun_couch_calm.png"

    show jun calm

    # Jun's inner thoughts continue
    "But really, talking to a boy? I know she’s in college now, but she’s so introverted that I worry about her. She might fall for an idiot."
    jun "What can we do? We have to stay quiet, of course. It feels like these gates have turned the world upside down overnight."
    
    show aditi stand_worried

    aditi "And these monsters... they're like nightmares come to life."
    "Yeah. I worry about her. She might get scared of some fool and agree to be with him."

    image jun sad = "images/assets/character_sprites/jun/scene_1_jun_couch_sad.png"

    show jun sad

    jun "Do you... think she's...?"

    image bg photo = "images/assets/cg/scene_1_three_siblings_photo.png"

    scene bg photo

    # Jun's inner thoughts about Akshara
    "I haven’t been contacted by my eldest sister, Akshara, after the monster invasion began. And let me tell you, she was married to a fool. (I can’t have that happening again.)"
    "She is, like 15 years older than me. She’s cool, but alone in this super apocalyptic situation…?"
    "Honestly, I’m scared."

    scene bg jun_aditi

    image aditi annoyed = "images/assets/character_sprites/aditi/scene_1_aditi_stand_annoyed.png"

    # Music fades to a melancholic tone
    # play music "assets/music/melancholic_music.mp3" # Replace with the actual path to your music.
    
    # Aditi's thoughts about Akshara
    show aditi annoyed

    aditi "No. Sister Akshara is out there somewhere. We just need to find her."

    image jun couch_2 = "images/assets/character_sprites/jun/scene_1_jun_couch_2.png"


    # Jun's inner thoughts about trusting Aditi
    "I feel a little better hearing that, somehow."
    "I trust Aditi’s judgment. She might not be the greatest at social interactions, but she does know her stuff. She’s like…book-smart. Top scorer and all that jazz."
    
    
    image aditi sit = "images/assets/character_sprites/aditi/scene_1_aditi_sit.png"

    image bg living_room_both_sit_1 = "images/assets/bg/scene_1_both_sit_bg_1.png" # Please replace with the actual path when you add the image.

    scene bg living_room_both_sit_1

    show aditi sit
    
    show jun couch_2

    "Aditi sits down next to me."
    aditi "I’m a bit scared too, you know. We could die tomorrow."
    aditi "Or today, if one of those mega-monsters appears here. We’d be crushed. Die without making a sound."

    # Jun and Aditi's reactions
    "My sister shudders."
    "I shudder too."
    
    show aditi sit

    aditi "But, you know, there’s a statistically low chance we will die. Only 10\% of the world has been affected right now…"
    "So, 1 person out of 10 has been killed, maimed, or otherwise afflicted by these monsters."
    "A comforting thought."

    image aditi cool = "images/assets/character_sprites/aditi/scene_1_aditi_sit_cool.png"

    show aditi cool

    show jun couch_2

    jun "Jeez, don’t you have anything nicer to talk about?"
    aditi "I don’t think so. But I do have something important to ask."

    image aditi sit_worried = "images/assets/character_sprites/aditi/scene_1_aditi_sit_worried.png"

    show aditi sit_worried

    aditi "A seal to close the Gates. I’ve been looking all over for it!"


    # Jun's reaction
    "I gulp. It’s always my fault when she gets like this."

    show aditi cool 
    aditi "Have you seen a piece of notebook paper lying around here, by any chance?"
    show jun couch_2 
    jun "No..?"
    show aditi sit_worried
    aditi "I kept it right here. What if someone took it? Or... what if it's lost forever?"
    jun "Why? What was on it?"

    # Music drops/gets darker
    # play music "assets/music/dark_music.mp3" # Replace with the actual path to your music.

    image jun surprised = "images/assets/character_sprites/jun/scene_1_jun_couch_surprised.png"
    
    show jun surprised 

    jun "Sister? You can close those Gates?"

    # Jun's reaction to Aditi's revelation
    "My sisters have always been literal geniuses…genii…whatever. But this? This? THIS?!"
    "I want to jump out of my seat and scream, but I can’t."
    "I can’t. I can’t. I can’t."
    "Aditi will freak out if I do that."

    image jun shocked = "images/assets/character_sprites/jun/scene_1_jun_couch_shocked.png"

    image aditi stern = "images/assets/character_sprites/aditi/scene_1_aditi_sit_stern.png"

    show aditi sit
    # Aditi's explanation
    aditi "Well, not exactly… I don’t know if I really can… But Akshara told me something a couple weeks ago that really stuck with me. And I used that to write the seal."
    
    show aditi cool
    aditi "It’s not tested yet, so don’t take my word for it. But still, I think…"
    "There she goes again, putting herself down…Wait! That’s not important right now!"
    
    show jun shocked
    jun "Sister, there are thousands of people researching a way to close the Gates, and you’re saying you…"
    
    show aditi stern
    aditi "Jun! Akshara was a physicist, so she was researching this stuff too. She was actually doing it for a while before the Gates, I think."
    
    show aditi sit_worried
    aditi "Only now… with the seal gone… I don’t know if I can make it again. And what if someone stole it?"

    show jun couch_2
    jun "Sis. You’re smart. You can totally make the seal again, right? Right?"
    "Don’t tell me…"

    show aditi sit
    aditi "Well…uhh…"

    image aditi shiftingeyes = "images/assets/character_sprites/aditi/scene_1_aditi_sit_shiftingeyes.png"

    # Jun's reaction to Aditi's eccentricity
    show jun couch_2
    jun "You didn’t make any notes, did you?"

    show aditi shiftingeyes
    aditi "Jun, you really don’t know what it’s like -"
    show jun couch_2
    jun "I don’t. That’s why I always tell you, I can’t help you if you don’t have a backup."
    "Sister always does things without a backup. And of course, every time it comes crashing down. I love the fact that she’s a genius. I don’t love that she’s eccentric about it."

    image aditi frantic = "images/assets/character_sprites/aditi/scene_1_aditi_sit_frantic.png"

    # Jun and Aditi's discussion about the seal's importance

    image jun worried = "images/assets/character_sprites/jun/scene_1_jun_couch_2.png"

    show jun worried
    jun "What if a monster stole it? Those things are sentient. They said that on TV."
    show aditi frantic
    aditi "Oh no…"

    image jun frantic = "images/assets/character_sprites/jun/scene_1_jun_couch_frantic.png"

    show jun frantic

    # Jun's attempt to comfort Aditi
    "Oh no. I can’t stand it when she gets like this. She’s been so much better about it recently too."
    "I have to do something. I panic and raise my hands."
    jun "Remember this?"

    # Illusion of the beach sunset scene
    image bg beach_sunset = "images/assets/bg/scene_1_both_sit_bg_2.png" # Please replace with the actual path when you add the image.

    scene beach_sunset
    # play sound "assets/sound/waves_crashing.mp3" # Replace with the actual path to your sound.

    image jun embarrassed = "images/assets/character_sprites/jun/scene_1_jun_couch_embarrassed.png"

    image jun sweatdrop = "images/assets/character_sprites/jun/scene_1_jun_couch_sweatdrop.png"

    image aditi calming = "images/assets/character_sprites/aditi/scene_1_aditi_sit_calming.png"

    show jun couch_2
    jun "That vacation a year ago was amazing, wasn’t it? Mumbai has the greatest beaches -"
    show aditi sit
    aditi "Not the cleanest ones."
    "It’s kinda annoying, you know? When you try to help someone and they just…"
    "Okay. I admit it. My representation of a beach is not exactly accurate."
    show jun sweatdrop 
    jun "Well, the expensive beaches are plenty clean."
    show aditi calming
    aditi "You’re so cute."

    show jun embarrassed
    jun "Sister!"

    # Broadcast bell rings
    # play sound "assets/sound/broadcast_bell.mp3" # Replace with the actual path to your sound.
    broadcast "Attention! A new gate has opened in the vicinity. Residents are advised to stay indoors."

    show jun sad

    "Oh no."
    "Oh no."
    "Oh no."

    # Fading back to the living room ambiance
    scene living_room_both_sit_1
    # play music "assets/music/living_room_ambiance.mp3" # Replace with the actual path to your music.

    # Return to main script
    return
