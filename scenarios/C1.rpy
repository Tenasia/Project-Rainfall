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
    show rain_particle
    nvl show
    n_nvl "Thunder streaked across the dull, pitch-black sky over the outskirts of an urban city. It overpowered all other sounds for an instant, but soon the clatter of rainwater against pavement blanketed the area once again. Even amongst the heavy downpour at night, bustles of pedestrians from the major streets could still be heard."
    n_nvl "However, no human presence resided within this small alleyway. There were little more than rat-infested decrepit buildings and the occasional ruffian fights inside. Because of that, the average person would find no reason to ever enter. And during this downpour, even the unsavory people would rather avoid causing trouble unnecessarily."
    n_nvl "Amidst this desolate space, the patter of rainwater was the only sign of motion. They collect into small crevices on the ground and eventually plunge into the gutter. However, they were not clear in color but contaminated in hues of crimson."
    nvl clear
    nvl show
    n_nvl "The shade grew darker the closer it was to the source. At the center of that source lay a motionless object on the ground. It had the shape of a human, yet it was unmoving."
    n_nvl "It was a corpse."
    n_nvl "The body was laid on its back. A young man with black hair, with a gruesome gash that pierced straight to the heart. Its mouth and eyes were both agape in twisted agony as if cursing the sky."
    n_nvl " Its blood continually seeped out from the hole, perpetually cleansed by the falling rain. Was it an act of mercy, or one of torture, it would never know. For even the final proof of the life it once held would all be drained away when the sky clears."
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
    noname_nvl "\"Another one, huh.\""
    nvl clear
    nvl hide 
    stop music fadeout 1.0
    scene black
    with fade
    pause 1.0
    $ nvl_mod = False

label ch2:
    scene bg a_alleyway
    with fade
    python:
        set_info_scene("01")
        set_info_location("02")
        set_info_date(10, "Sep", "thu")
        set_info_time("evening")
    play music audio.window fadein 3.0
    n_adv "Thursday 17:53. September 10, 2012"
    n_adv "The time and date popped up as I moved the mouse cursor. I leaned back on the chair and stretched my arms wide to let my stiffened joints relax. Finally, the most awaited time of the day, the end of the work schedule."
    n_adv "I glanced around the office room. As usual, there were only a couple of guys left. Most employees in my section finish at 17:30. Those who stayed late were either backed up or took on overtime. Let’s just say I’m part of the former."
    n_adv "Usually, I would’ve lingered even longer, but a nasty headache assaulted me earlier. I’ll take it a little easier today."
    play ambient "longrain" fadein 0.5
    n_adv "{i}Tap tap tap{/i}"
    n_adv "Misty droplets knocked on the windowpanes. It was drizzling outside."
    n_adv "Dark orange hues casted shadows on the sky. By the time I finished preparing to leave, the sun had completely dipped under the horizon."
    
    Takumi "\"I’m going ahead, see you on Monday.\""
    Coworker "\"Good work, Ito-san. Going home a bit early today?\""
    Takumi "\"Yeah, got a nasty headache.\""
    Coworker "\"I see, alright. Get some rest, and don't forget anything.\""
    Takumi "\"Sure, sure.\""
    n_adv "With my backpack in tow, I took the stairs to the ground floor. The building was pretty large for an office building. It was relatively new as well, acquired just last year by my employer."
    stop ambient fadeout 0.5
    play ambient "lightrain" fadein 0.5 volume 0.75
    scene bg a_alleyway
    with fade
    n_adv "At the entrance section, our security guard sat behind a wooden desk, eyes glued to his phone. Noticing me, he glanced up and gave a small nod before returning to being engrossed in his screen."

    
    n_adv "As I reached the front door, the noise of the rain had grown considerably louder."
    Takumi "\"{i}Sigh{/i}\""
    n_adv "It’s not that I disliked rain in general, but walking around puddles was annoying. On these occasions, I silently thanked the company for picking a location only a few blocks away from the metro station."
    n_adv "But there was still another problem. It wasn’t currently the rainy season, so I didn’t prepare an umbrella."
    Takumi "\"...Ah, right.\""
    n_adv "Fortunately, they kept a stock of spare umbrellas employees can borrow for these situations."
    Takumi "\"Nakamura-san, can I borrow an umbrella?\""
    n_adv "The security guard glanced up again."
    Nakamura "\"Sure\""
    n_adv "Without even turning, he extended an arm and rummaged around the cabinet behind him. Grabbing one at random, he handed it to me."
    Nakamura "\"Return it by Monday, yeah?\""
    n_adv "I gratefully accepted the umbrella."
    Takumi "\"Will do, thanks.\""
    n_adv "Just as I was about to pull the doorknob, he called out again."
    Nakamura "\"Also, be careful on your way home.\""
    Takumi "\"Why, what happened?\""
    n_adv "After a pause, he set his phone down on the table."
    Nakamura "\"Apparently, crimes have been increasing recently.\""
    n_adv "My eyebrows raised at his words. Japan was one of the safest countries in the world, everyone knew that. If Nakamura was saying that…do I need to be worried?"
    Nakamura "\"Well, probably just some drunken scuffles. Those happen all the time. Don’t worry about it too much as long as you don’t go looking for trouble.\""
    Takumi "\"...I’ll keep that in mind, thanks for the heads up.\""
    n_adv "I took my phone out and noted the info down. I forget things easily, so noting things down helps a lot. Once finished, I bid him a good evening and stepped out."

    stop ambient fadeout 1.0
    play ambient "rain" fadein 1.0
    scene bg cram_hallway
    with fade
    n_adv "At some point during our conversation, the sky had turned dark. The rain turned out to be lighter than expected, which was great."
    n_adv "I glanced at the bright LED signpost above the door frame. ‘Yasuda Farmers’, it read. I’ve commuted here daily for the past few months, yet today these familiar streets felt a little chillier than usual."
    Takumi "\"What am I, five?\""
    n_adv "Chiding myself, I brushed Nakamura’s words off my mind. I slowly made my way towards the busy intersection road that connected to the metro station."

    scene bg road_school
    with fade 
    n_adv "It wasn’t until I saw the headlights of passing cars and pedestrians that I let out a breath of relief. There really was a form of comfort from being surrounded by people."
    n_adv "The secluded alleyway opened up into a much larger street lined with various office buildings and the occasional eye-catching signboards of restaurant chains."
    n_adv "Every day, during rush hours, salary workers bustled around these areas, and today was no exception."
    n_adv "I shimmied my way into the flow of pedestrians towards the station. My umbrella kept bumping into others’, but that’s just how it was during rush hour."
    n_adv "Actually, it was kind of remarkable just how densely packed it was here when there was nobody just a corner away earlier."
    n_adv "Either way, now within a crowded space and a straight road ahead, I let my thoughts wander a little. What should I have for dinner tonight…"
