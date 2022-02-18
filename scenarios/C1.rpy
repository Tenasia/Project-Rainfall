label ch1:
    $ notebook_info = None
    $ nvl_mod = True
    stop music fadeout 1.0
    with fade
    scene black 
    pause 2.0
    play music audio.dark fadein 2
    play ambient "rain" fadein 1
    play se "thunder" fadein 0.5
    scene bg a_alleyway
    with fade
    show rain_particle
    narrator "Thunder streaked across the dull, pitch-black sky over the outskirts of an urban city. It overpowered all other sounds for an instant, but soon the clatter of rainwater against pavement blanketed the area once again. Even amongst the heavy downpour at night, bustles of pedestrians from the major streets could still be heard."
    narrator "However, no human presence resided within this small alleyway. There were little more than rat-infested decrepit buildings and the occasional ruffian fights inside. Because of that, the average person would find no reason to ever enter. And during this downpour, even the unsavory people would rather avoid causing trouble unnecessarily."
    narrator "Amidst this desolate space, the patter of rainwater was the only sign of motion. They collect into small crevices on the ground and eventually plunge into the gutter. However, they were not clear in color but contaminated in hues of crimson. The shade grew darker the closer it was to the source. At the center of that source lay a motionless object on the ground. It had the shape of a human, yet it was unmoving."
    nvl clear
    nvl show
    narrator "It was a corpse."
    narrator "The body was laid on its back. A young man with black hair, with a gruesome gash that pierced straight to the heart. Its mouth and eyes were both agape in twisted agony as if cursing the sky. Its blood continually seeped out from the hole, perpetually cleansed by the falling rain. Was it an act of mercy, or one of torture, it would never know. For even the final proof of the life it once held would all be drained away when the sky clears."
    nvl clear
    
    scene black
    with fade
    stop se fadeout 0.5
    $ renpy.pause(0.5, hard = True)
    play se "sudden_thunder" fadein 0.0 volume 1
    $ renpy.pause(0.5, hard = True)
    scene white 
    pause 1
    scene black
    with dissolve
    stop ambient
    stop se
    pause 2.0
    
    nvl show
    unknown "\"Another one, huh.\""

    nvl clear
    stop music fadeout 1.0
    scene black
    with fade
    pause 1.0
    $ nvl_mod = False

    scene bg a_alleyway
    with ComposedTransition(dissolve)

label ch2:
    python:
        set_info_scene("01")
        set_info_location("02")
        set_info_date(10, "Sep", "thu")
        set_info_time("evening")
    play music audio.window fadein 2
    Fuuji "test"
    Fuuji "test"
    Fuuji "test"
    Fuuji "test"
    Fuuji "test"
