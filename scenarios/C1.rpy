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
    # stop ambient fadeout 1.0
    # stop music fadeout 1.0
    # stop se fadeout 1.0
    stop ambient fadeout 1.0
    play music audio.kamikaze fadein 1.0 
    play se "car_horn"
    Takumi "\"...?\"" 
    play se "watersplash"
    Takumi "\"Ahk!?\""
    n_adv "Suddenly, ice-cold water blasted my legs. Bewildered, I glanced around. A black sedan rushed past me, spraying puddles of water in its wake. Several other pedestrians yelped in surprise and anger alike."
    n_adv "Oi, oi, there’s no way that’s within the speed limit! Not to mention, it was driving in the opposite lane!"
    n_adv "I suppressed the urge to curse out loud as it zipped through traffic, much to the dismay of the other drivers who honked in protest. Eventually, it made a sharp turn onto a bridge and swerved out of vision."
    stop music fadeout 1.0
    play music audio.window fadein 1.0
    play ambient "rain" fadein 2.0
    Takumi "\"...\""
    n_adv "Man, some people shouldn’t be allowed a driving license. Damned irresponsible drivers."
    n_adv "I assessed the damage done. My shoes were completely drenched and my trousers soaked up to the knees. And if the weight of the patter on my umbrella was any indication, the rain was only getting more intense."
    n_adv "The evening had barely just begun and it already got a whole lot worse."
    Takumi "\"{i}...Sigh.{/i}\""
    n_adv "Begrudgingly, I walked the rest of the way with damp, near-freezing soles. And this time, I had to be cautious of idiots behind steering wheels too."
    stop music fadeout 1.0
    stop ambient fadeout 1.0

label ch3:
    scene bg a_alleyway
    with fade
    play music audio.tokyo
    play ambient "rain_inside_car" fadein 1.0
    n_adv "A pleasant tune hummed from the radio, my feet tapping along to it. The chilly night breeze flowed in through the open window, inviting along stray drops of rainwater to trickle in."
    n_adv "A radar speed gun was propped on the window frame, supported by a makeshift harness. With each passing vehicle, the red digital numbers fluctuated slightly."
    n_adv "Munching on a biscuit, I peered into the open sky as rows upon rows of buildings gradually lit up, signaling the shift into the ever-familiar scene of a nighttime metropolis."
    n_adv "My car was parked in an empty lot by the roadside, just behind an intersection. The engine was turned off."
    n_adv "Being a cop had its ups and downs. Sometimes I had to fill out headache-inducing paperwork. Other times, I get to relax while watching numbers fluctuate. Today was one of the latter. As part of my patrol routine, I was stationed here."
    n_adv "I peeked inside the box of biscuits strewn on the passenger seat. Yeah... five pieces wouldn’t last me through the remaining two hours of my shift. These packaging sizes were getting more and more outrageously misleading."
    n_adv "I know I said patrolling was relaxed and nice, but there was still one major challenge present. Namely, boredom. There’s only so many passing vehicles you can stare at before your mind starts to get numb."
    n_adv "I stretched my palm out the window, letting the raindrops revitalize my sore muscles. Maybe I should stop by a convenience store, I thought as I grabbed another biscuit. Either that, or I hope something interesting happens tonight."
    Hiraku "\"...?\""
    n_adv "Out of the corner of my vision, I spotted a young man sporting a red traditional hakama walking by the roadside. Accompanied by several men in black suits, he turned heads wherever he passed."
    n_adv "What an odd outfit in this day and age. Was there some kind of festival going on? Before long, they disappeared into a corner."
    Hiraku "\"Hmm..\""
    n_adv "I couldn’t quite put my finger on it, but his outfit looked familiar. Where had I seen him before? Just as I was trying to jog my memory, something else caught my attention."
    
    stop music fadeout 1.0
    play music audio.kamikaze fadein 1.0

    n_adv "Through the rearview mirror, I noticed a sedan bolting through the street at high speed, swerving around oncoming traffic. That...didn’t even require a radar confirmation. It was clearly far above the speed limit!"
    n_adv "I got up to action immediately."
    n_adv "Just as a formality and for the paperwork registration later, I pointed the radar towards the car anyway. 81 — it registered — on a 60 zone freeway. Following proper procedure, I picked up the transceiver and switched the mic on."
    Hiraku "\"HQ, you there? Inoue Hiraku from patrol car 17 here.\""
    n_adv "After a slight pause, a static voice replied."
    play se "static" fadein 1.0
    Radio "\"Inoue-san, this is Tenma Station. What’s the matter?\""
    Hiraku "\"I’m on patrol around West Tenma, and there’s a black sedan recklessly speeding. Can I get some roadblocks assistance?\""
    Radio "\"Can you tell us the car model and license plate number?\""
    n_adv "I squinted to get a better look, but the glare was too bright and the sedan was swerving too much."
    Hiraku "\"I can’t get a good look.\""
    n_adv "Even as it approached the intersection, it showed no signs of slowing down."
    Hiraku "\"...!\""
    n_adv "The sedan nearly brushed against another car as it switched lanes. My body tensed up. That’s just too reckless! Soon it would overtake my position."
    Radio "\"Negative. The nearest available cruiser is five kilometers to your southeast.\""
    n_adv "Huh. Normally, there should’ve been at least another patrol unit in this area. Were they all occupied? Either way, boredom was about to become the least of my worries tonight."
    Hiraku "\"Then, requesting permission to engage in a pursuit.\""
    n_adv "Speeding on a country road was one thing, but on a busy street? Like hell I was about to let this guy loose. There was a pause, and then I heard a low groan from the transceiver."
    n_adv "I knew they would rather avoid a pursuit if they could help it, that’s just how our system was. However, that would mean letting the lawbreaker unpunished."    
    play se "watersplash" fadein 0.5
    n_adv "In a blur, the sedan darted past my position, spraying water onto my windshield."
    Hiraku "\"This guy..!\""
    n_adv "The gall!"
    n_adv "With a loud skid, it sharply turned left on the intersection ahead, leaving behind a messy scene of honking and braking cars."
    n_adv "I unclasped the speed gun and threw it onto the passenger seat. Revving the engine up, I waited in bated breath. Cmon, say the magic word already."
    n_adv "HQ finally responded in resignation."
    Radio "\"Pursuit authorized. We will provide directional assistance from HQ.\""
    stop music fadeout 1.0
    play music audio.blue fadein 1.0
    n_adv "A smirk rose to my lips."
    Hiraku "\"Roger that.\""
    n_adv "Putting the transceiver back in its slot, I flicked on one of the numerous switches in the middle compartment. In response, the speaker on the roof activated and started blaring the ever-familiar wail of police siren."
    n_adv "Without waiting for another second, I stepped on the gas pedal. The evening’s about to get a whole lot rowdier. The car skidded off as I turned the corner in pursuit of the sedan."
    scene bg a_alleyway
    with fade
    n_adv "Upon hearing the siren, the other cars began to part away, opening a clear path in the middle for me."
    Hiraku "\"Heh.\""
    n_adv "As a teen, I’ve always fantasized about this. And even after seven years, the feeling never gets old. I pressed the pedal even lower."
    play se "gear_shift" fadein 1.0
    play ambient "car_on_road" fadein 1.0
    n_adv "My chest tightened from the sheer pressure of inertia. Silhouettes of the city skyline flew past quicker and quicker as my car rapidly accelerated."
    Hiraku "\"...!\""
    n_adv "I could finally spot the sedan! It was quite far ahead, still swerving wildly around traffic, but I was slowly gaining ground!"
    play se "gear_shift" fadein 1.0
    n_adv "I kicked the clutch as I pushed for even faster. The rain blocked my vision a little, but I’ve had my fair share of similar situations. Just had to rely on familiarity."
    n_adv "Keeping my eyes focused ahead, I chased after the fleeing black sedan."
    Hiraku "\"...!\""
    n_adv "The license plate was coming into sight!"
    Hiraku "\"HQ, here’s the license plate! Chi(ち) 6… 3… 1… and…7!\""
    Radio "\"That license plate is unregistered.\""
    Hiraku "\"Unregistered?\""
    n_adv "Damnit, did I get it wrong? I squinted once more."
    Hiraku "\"...!\""
    n_adv "No, it wasn’t that I got it wrong, but rather—"
    Hiraku "\"It’s a paper plate!\""
    n_adv "There’s only ever two reasons a car would have one. Either it’s brand new…or the car’s being used for illegal purposes. Either way, looks like pursuit was the right call."
    n_adv "The sedan took another sharp turn, and I followed suit."
    Hiraku "\"...!\""
    n_adv "Over in the next crossroad, the traffic lights just turned red. The sedan wasn’t slowing down in the slightest. Did it plan to run through?"
    Radio "\"Inoue-san, we’re switching the traffic lamp back to green!\""
    Hiraku "\"Thanks!\""
    n_adv "Even so, it’s still absurdly dangerous. I pressed a button on the dashboard."
    Hiraku "\"This is the police!\""
    n_adv "My voice blared through the speaker above."
    Hiraku "\"Pull over your car! I repeat, this is the police! Pull over your—\""
    Hiraku "\"!!!\""
    n_adv "Right before the lights turned back green, a bus appeared from the left side of the junction! My eyes widened in horror."
    n_adv "The sedan was still going at full speed, running headfirst into the bus! What’s it gonna do!? What should I do!?"
    n_adv "Hesitantly, I released the gas pedal. But what about the sedan?"
    n_adv "Finally noticing the rampant sedan, the bus pumped on the brakes, tires grinding into asphalt."
    play se "car_horn"
    n_adv "But the sedan was already too close! It was too late!"
    Hiraku "\"!?\""
    n_adv "But instead of braking…the sedan swerved right!"
    n_adv "By a hair’s breadth, it bolted past the front of the bus…and managed to slip through! The bus ground to a halt just in the nick of time."
    n_adv "The sedan raced all the way to the other end of the intersection. Tires screeched as a whole line of cars ahead had to pump their brakes."
    Hiraku "\"Crazy bastard ...tsk!\""
    play se "gear_shift"
    n_adv "My heart hammering, I banked on the clutch and stepped back on the gas pedal. Using the opening the sedan created, I barreled past the bus, past the headlights of stunned drivers, and…made it through!"
    Hiraku "\"Sorry, everyone!\""
    n_adv "My voice blared one last time before I switched the microphone off. This sedan driver was insane! It’s practically a miracle we didn’t collide into anything. I could only pray nobody else crashed back there."
    scene bg a_alleyway
    with fade
    n_adv "As we entered this relatively empty road, the sedan began to accelerate in a straight line. Trying to beat me in a contest of speed?"
    Hiraku "\"You wish.\""
    play se "gear_shift"
    n_adv "I floored the pedal in response, the accelerometer needle soaring. The city skyline outside blended into a long string of blur."
    n_adv "Passing through intersection after intersection, the sedan kept going straight. Had it given up on shaking me off? The gap was gradually closing once more."
    Radio "\"Inoue-san, it looks like the sedan is trying to escape to Yodogawa Ward through Nagara Bridge. We’ve already contacted their police station. They’re prepared to intercept at their end of the bridge. We need you to lead him to that point.\""
    Hiraku "\"Nagara Bridge… Roger, I’ll keep pressuring them from this side.\""
    n_adv "The game of tag continued as our cars darted down the road at blazing speeds. Rain droplets on my windshield cascaded into parting trails, swept away by the rushing wind. Without any of the twists and turns, gripping the steering wheel almost felt…serene, peaceful."
    Hiraku "\"...\""
    scene bg a_alleyway
    with fade
    n_adv "The sedan blazed through the final intersection leading to the bridge."
    n_adv "Past this point, there was nowhere else to go. All I had to do was leisurely follow behind. I slowed down a little, wiping the sweat off my brow. My tense shoulders finally got a chance to relax."
    n_adv "I was nearing the limit of my focus. Especially after that close encounter earlier."
    scene bg a_alleyway
    with fade 
    Hiraku "\"The sedan has reached the bridge. I repeat, the sedan is on the bridge.\""
    Radio "\"Good work, Inoue-san. Standby over there in case it tries to turn around.\""
    Hiraku "\"Roger.\""
    n_adv "From the edge of my vision, I spotted two police SUVs at the end of the bridge blocking the path. There’s no space for the sedan to pass through. It’s checkmate! I could already imagine the newspaper headlines."
    n_adv "..."
    stop music fadeout 1.0
    play music audio.strike fadein 1.0
    n_adv "But…the sedan wasn’t slowing down."
    Hiraku "\"...?\""
    n_adv "That’s strange. The roadblock was definitely visible from there. Was it not paying attention?"
    n_adv "The sedan flew through the bridge at full speed. What’s it trying to do? If it keeps going…there’s nothing but a crash awaiting!"
    Hiraku "\"No way...\""
    stop ambient fadeout 1.0
    play ambient "rain" fadein 1.0
    stop music fadeout 1.0
    n_adv "The officers on the other side were holding up megaphones, warning the sedan to slow down. However, their words fell on deaf ears."
    n_adv "The asphalt rattled as the sedan showed no signs of slowing."
    n_adv "My face morphed into one of horror. My eyes couldn’t avert the scene as the crash quickly became imminent."
    n_adv "The officers scrambled to dive out of the way, panic reflected in their eyes. Screaming ensued."
    n_adv "Time slowed down for an instant as the sedan inched nearer…nearer..!"
    n_adv "And then came the moment of impact."
    play se "car_crash" fadein 1.0 volume 0.5
    scene black
    pause 3.0
    with fade
    stop ambient
