label ch1:
    
    $ notebook_info = None
    $ nvl_mod = True
    stop music fadeout 1.0
    with fade
    scene black 
    pause 2.0
    play music audio.door fadein 2
    play ambient "rain" fadein 1
    play se1 "thunder" fadein 0.5
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
    stop se1 fadeout 0.5
    $ renpy.pause(0.5, hard = True)
    play se1 "sudden_thunder" fadein 0.0 volume 1
    $ renpy.pause(0.5, hard = True)
    scene white 
    pause 1
    scene black
    with dissolve
    stop ambient
    stop se1
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

    python:
        set_info_scene("02")
        set_info_location("02")
        set_info_date(10, "Sep", "thu")
        set_info_time("evening")

    scene placeholder
    with fade
    pause 2.0
    
    scene bg office_eve
    with fade
    play music audio.window fadein 3.0

    $ show_date()
    
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
    scene bg office_entrance_eve
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
    scene bg office_outside_raining
    show rain_particle
    with fade
    play ambient "rain" fadein 1.0

    n_adv "At some point during our conversation, the sky had turned dark. The rain turned out to be lighter than expected, which was great."
    n_adv "I glanced at the bright LED signpost above the door frame. ‘Yasuda Farmers’, it read. I’ve commuted here daily for the past few months, yet today these familiar streets felt a little chillier than usual."
    Takumi "\"What am I, five?\""
    n_adv "Chiding myself, I brushed Nakamura’s words off my mind. I slowly made my way towards the busy intersection road that connected to the metro station."

    scene bg street_night
    show rain_particle
    with fade

    python:
        set_info_location("03")
    
    n_adv "It wasn’t until I saw the headlights of passing cars and pedestrians that I let out a breath of relief. There really was a form of comfort from being surrounded by people."
    n_adv "The secluded alleyway opened up into a much larger street lined with various office buildings and the occasional eye-catching signboards of restaurant chains."
    n_adv "Every day, during rush hours, salary workers bustled around these areas, and today was no exception."
    n_adv "I shimmied my way into the flow of pedestrians towards the station. My umbrella kept bumping into others’, but that’s just how it was during rush hour."
    n_adv "Actually, it was kind of remarkable just how densely packed it was here when there was nobody just a corner away earlier."
    n_adv "Either way, now within a crowded space and a straight road ahead, I let my thoughts wander a little. What should I have for dinner tonight…"
    
    stop ambient fadeout 1.0
    play music audio.kamikaze fadein 1.0 
    play se1 "car_horn"
    play se2 "watersplash"

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
    scene black
    with fade
    pause 2.0

label ch3:

    python:
        set_info_scene("03")
        set_info_location("04")
        set_info_date(10, "Sep", "thu")
        set_info_time("evening")

    scene placeholder
    with fade
    pause 2.0
    
    scene bg car_night_rain
    with fade
    play music audio.tokyo
    play ambient "rain_inside_car" fadein 1.0 volume 0.25
    
    $ show_date()
 
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
    
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    play music audio.kamikaze fadein 1.0

    n_adv "Through the rearview mirror, I noticed a sedan bolting through the street at high speed, swerving around oncoming traffic. That...didn’t even require a radar confirmation. It was clearly far above the speed limit!"
    n_adv "I got up to action immediately."
    n_adv "Just as a formality and for the paperwork registration later, I pointed the radar towards the car anyway. 81 — it registered — on a 60 zone freeway. Following proper procedure, I picked up the transceiver and switched the mic on."
    Hiraku "\"HQ, you there? Inoue Hiraku from patrol car 17 here.\""
    
    play se1 "static" fadein 1.0
    
    n_adv "After a slight pause, a static voice replied."
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
    
    play se1 "watersplash" fadein 0.5
    
    n_adv "In a blur, the sedan darted past my position, spraying water onto my windshield."
    Hiraku "\"This guy..!\""
    n_adv "The gall!"
    n_adv "With a loud skid, it sharply turned left on the intersection ahead, leaving behind a messy scene of honking and braking cars."
    n_adv "I unclasped the speed gun and threw it onto the passenger seat. Revving the engine up, I waited in bated breath. Cmon, say the magic word already."
    n_adv "HQ finally responded in resignation."
    Radio "\"Pursuit authorized. We will provide directional assistance from HQ.\""
    
    stop music fadeout 2.0
    play music audio.blue fadein 2.0
    play ambient "car_on_road"
    
    n_adv "A smirk rose to my lips."
    Hiraku "\"Roger that.\""
    n_adv "Putting the transceiver back in its slot, I flicked on one of the numerous switches in the middle compartment. In response, the speaker on the roof activated and started blaring the ever-familiar wail of police siren."
    n_adv "Without waiting for another second, I stepped on the gas pedal. The evening’s about to get a whole lot rowdier. The car skidded off as I turned the corner in pursuit of the sedan."
    
    scene bg road1_night
    show rain_particle
    with fade
    
    python:
        set_info_location("05")
    
    n_adv "Upon hearing the siren, the other cars began to part away, opening a clear path in the middle for me."
    Hiraku "\"Heh.\""
    n_adv "As a teen, I’ve always fantasized about this. And even after seven years, the feeling never gets old. I pressed the pedal even lower."
    
    play se1 "gear_shift"
    play ambient "car_on_road" fadein 1.0
    
    n_adv "My chest tightened from the sheer pressure of inertia. Silhouettes of the city skyline flew past quicker and quicker as my car rapidly accelerated."
    Hiraku "\"...!\""
    n_adv "I could finally spot the sedan! It was quite far ahead, still swerving wildly around traffic, but I was slowly gaining ground!"
    
    play se1 "gear_shift"
    
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
    
    play se1 "truck_horn"
    
    n_adv "But the sedan was already too close! It was too late!"
    Hiraku "\"!?\""
    n_adv "But instead of braking…the sedan swerved right!"
    n_adv "By a hair’s breadth, it bolted past the front of the bus…and managed to slip through! The bus ground to a halt just in the nick of time."
    n_adv "The sedan raced all the way to the other end of the intersection. Tires screeched as a whole line of cars ahead had to pump their brakes."
    Hiraku "\"Crazy bastard ...tsk!\""
    
    play se1 "gear_shift"
    
    n_adv "My heart hammering, I banked on the clutch and stepped back on the gas pedal. Using the opening the sedan created, I barreled past the bus, past the headlights of stunned drivers, and…made it through!"
    Hiraku "\"Sorry, everyone!\""
    n_adv "My voice blared one last time before I switched the microphone off. This sedan driver was insane! It’s practically a miracle we didn’t collide into anything. I could only pray nobody else crashed back there."
    
    scene bg road2_night
    show rain_particle
    with fade
    
    n_adv "As we entered this relatively empty road, the sedan began to accelerate in a straight line. Trying to beat me in a contest of speed?"
    Hiraku "\"You wish.\""
    
    play se1 "gear_shift"
    
    n_adv "I floored the pedal in response, the accelerometer needle soaring. The city skyline outside blended into a long string of blur."
    n_adv "Passing through intersection after intersection, the sedan kept going straight. Had it given up on shaking me off? The gap was gradually closing once more."
    Radio "\"Inoue-san, it looks like the sedan is trying to escape to Yodogawa Ward through Nagara Bridge. We’ve already contacted their police station. They’re prepared to intercept at their end of the bridge. We need you to lead him to that point.\""
    Hiraku "\"Nagara Bridge… Roger, I’ll keep pressuring them from this side.\""
    n_adv "The game of tag continued as our cars darted down the road at blazing speeds." 
    n_adv "Rain droplets on my windshield cascaded into parting trails, swept away by the rushing wind. Without any of the twists and turns, gripping the steering wheel almost felt…serene, peaceful."
    Hiraku "\"...\""

    scene bg road3_night
    show rain_particle
    with fade

    n_adv "The sedan blazed through the final intersection leading to the bridge."
    n_adv "Past this point, there was nowhere else to go. All I had to do was leisurely follow behind. I slowed down a little, wiping the sweat off my brow. My tense shoulders finally got a chance to relax."
    n_adv "I was nearing the limit of my focus. Especially after that close encounter earlier."
    
    scene bg road4_night
    show rain_particle
    with fade 
    stop ambient fadeout 1.0

    Hiraku "\"The sedan has reached the bridge. I repeat, the sedan is on the bridge.\""
    Radio "\"Good work, Inoue-san. Standby over there in case it tries to turn around.\""
    Hiraku "\"Roger.\""
    n_adv "From the edge of my vision, I spotted two police SUVs at the end of the bridge blocking the path. There’s no space for the sedan to pass through. It’s checkmate! I could already imagine the newspaper headlines."
    n_adv "..."

    stop music fadeout 1.0
    scene bg bridge_night
    show rain_particle
    with fade
    play music audio.strike fadein 1.0
        
    python:
        set_info_location("06")

    n_adv "But…the sedan wasn’t slowing down."
    Hiraku "\"...?\""
    n_adv "That’s strange. The roadblock was definitely visible from there. Was it not paying attention?"
    n_adv "The sedan flew through the bridge at full speed. What’s it trying to do? If it keeps going…there’s nothing but a crash awaiting!"
    Hiraku "\"No way...\""
    
    play ambient "rain" fadein 2.0
    stop music fadeout 1.0
    
    n_adv "The officers on the other side were holding up megaphones, warning the sedan to slow down. However, their words fell on deaf ears."
    
    n_adv "The asphalt rattled as the sedan showed no signs of slowing."
    n_adv "My face morphed into one of horror. My eyes couldn’t avert the scene as the crash quickly became imminent."
    n_adv "The officers scrambled to dive out of the way, panic reflected in their eyes. Screaming ensued."
    n_adv "Time slowed down for an instant as the sedan inched nearer…nearer..!"
    n_adv "And then came the moment of impact."
    
    stop ambient fadeout 2.0
    play se1 "car_crash" fadein 1.0
    scene black
    with fade
    pause 2.0
    

label ch4:

    python:
        set_info_scene("04")
        set_info_location("07")
        set_info_date(10, "Sep", "thu")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene black
    with fade
    pause 2.0
    
    play se1 "gear_shift"

    n_adv "{i}Thud{/i}"

    scene bg train large
    with white3
    play ambient "inside_train" fadein 1.0
    
    $ show_date()


    n_adv "My water bottle fell over sideways. That jolted me awake."
    Takumi "\"...\""
    n_adv "Did I fall asleep? I picked the bottle up and rubbed my eyes. I was seated inside a train, my body swaying with the train’s rhythm. I retraced my steps to clear away the drowsiness."
    
    play se1 "train_passing" fadein 1.0
    
    n_adv "After that unpleasant experience earlier, I trudged the rest of the way to the metro station in wet trousers. There, I managed to wipe some of the water off with toilet paper."
    n_adv "My legs were still damp and freezing, and I could even smell a faint pungent odor. I silently apologized to the passengers around me."
    
    stop se1 fadeout 1.0
    play se1 "train_chime"
    
    Announcer "\"Attention, passengers. We have arrived at Shin-Imamiya Station. Please do not forget to take your belongings.\""
    n_adv "Eventually, the train reached a complete halt and the doors slid open."
    
    stop ambient fadeout 1.0
    scene bg station01 night
    with fade
    play ambient "lightrain" fadein 2.0
    play music audio.osmanthus fadein 1.0
    
    python:
        set_info_location("08")

    n_adv "I was greeted with the blanketing clatter of rainwater once again, shattering what respite I had inside the enclosed train car."
    n_adv "The doors slid shut behind me as I stepped off. It quickly accelerated again, the rails rattling along. I gazed listlessly as it gradually drifted out of sight to carry on with its nightly duties. In its place, only empty tracks remained."
    Takumi "\"...\""
    
    play se1 "clap"
    
    n_adv "{i}Clap{/i}"
    n_adv "What am I doing? I shouldn’t be zoning out right now. Perhaps the exhaustion was getting to me."
    
    scene bg station01 staircase
    with fade
    
    n_adv "The staircase led to the station lobby."
    
    scene bg train_entrance
    with fade 
    
    n_adv "As I was about to reach the exit, a peculiar sound entered my ears. My feet halted. It was a faint hymn of a...violin?" 
    n_adv "Even through the patter of rain, the melody carried over distinctly. It was a simple tune, yet something about it carried a hint of nostalgia."
    n_adv "My eyes searched for the source of the music and spotted a tiny crowd at the corner of the otherwise empty lobby. A busker? And a skilled one too, judging by the number of people listening."
    n_adv "Street performers weren’t uncommon in parks or near tourist spots. On occasions where time permitted, I’d let myself be enraptured by their melodies. There was something soothing about a gathering of strangers brought together by music."
    n_adv "The piece gradually concluded as the crowd softly applauded. A moment later, another melody began as the performer moved on to the next piece."
    Takumi "\"...\""
    n_adv "On a better day, I might’ve joined the audience. But today…I was quite exhausted. My freezing ankles and grumbling stomach protested."
    n_adv "…Yeah, it’s a shame, but let’s head home straight away."
    
    stop ambient fadeout 2.0
    scene bg road night large
    show rain_particle
    with fade 
    play ambient "rain" fadein 2.0

    python:
        set_info_location("09")
    
    n_adv "The exit opened up to a spacious but dimly-lit street I’ve been through a million times." 
    n_adv "My apartment was only five minutes away by foot, but that’s about the only good thing it had going for it. The neighborhood I lived in wasn’t particularly well-cared for."
    n_adv "I glanced at the streetside opposite of the station, beyond the crosswalk I normally use. As if to prove my point, garbage bags were littered around the pavement."
    Takumi "\"{i}...Sigh.{/i}\""
    n_adv "On days leading up to the cleaning day, it’s always like this. Repulsed by the rancid smell it would’ve no doubt been oozing, I decided to walk further in search of another crosswalk."
    n_adv "I let my thoughts wander aimlessly as my legs skirted around puddles on the walkway."
    n_adv "There’s a reason I disliked my apartment despite the convenient location, and it’s one I could never stop worrying about. Namely, because it was located within one of the shadiest districts in the prefecture."
    n_adv "Historically, this district has one the highest crime rates across the whole country. Well, it’s not like I couldn’t understand the reason. One glance at the neighborhood and you could tell the living conditions of its inhabitants."
    n_adv "At night, there were even occasions where I could hear gunshots and—"
    n_adv "My thoughts were interrupted by the sound of snoring. I looked around to find a person laying on a bench nearby with a raincoat on."
    Takumi "\"...\""
    n_adv "As much as I wanted to be disgusted by it, I’d grown numb to the sight of the homeless. Though, how they were able to sleep under heavy rain was beyond me. I heaved a sigh and continued walking."
    n_adv "I reached the next crosswalk and pressed the pedestrian crossing button absentmindedly. The light instantly flickered green."
    Takumi "\"...\""
    n_adv "Under the dim lamppost, I peered into the furthest reaches of the street. It was devoid of even the faintest vehicle light."
    n_adv "…Was there even a point in pressing it? As I crossed the desolate street, my mind drifted to the conversation I had with Nakamura earlier at work."
    Takumi "\"Increasing crime rates, huh...\""
    n_adv "When he mentioned it, I couldn’t help but be worried. It reminded me of an old rumor I heard from the elderly folk."
    n_adv "Long ago, this district used to be a yakuza group’s home turf. They controlled everything, from the entirety of the land to the lives of the residents themselves."
    n_adv "Over the years, following stricter and stricter laws, they dwindled away and the residents regained their freedom. However, they didn’t disappear without leaving their mark."
    n_adv "Many blamed the current state of the district on the yakuzas of old. Some radicals even believed that there were active yakuza insurgents."
    n_adv "Of course, they’re nothing more than rumors. However, each time a loud noise jolts me awake in the dead of night, those rumors would float to my mind."
    Takumi "\"...Ah\""
    n_adv "Without realizing it, I’d reached my destination."
    
    scene bg takumi_house
    show rain_particle
    with fade

    python:
        set_info_location("10")

    n_adv "This dingy little building with stained walls and crooked handrail was my home. I’ve lived here almost my whole life."
    n_adv "Near my feet lay a broken mailbox post, rusted and collapsed. It hadn’t been repaired for nearly five years. Nor was there any need to."
    n_adv "Physical mails were slowly fading away, replaced by digital mails. It’s a testament of the shifting ages we lived in."
    Takumi "\"...\""
    n_adv "This building, too, had seen better days. I pictured it exactly as it looked a decade ago, fresh coat of paint and glossy steel."
    n_adv "As a kid, I used to roam these streets a lot. Alongside my brother, we played with the other neighborhood kids. At noon, mom would welcome us home with a warm plate of food."
    Takumi "\"...\""
    n_adv "The harsh patter of rain on my umbrella brought me back to reality."
    n_adv "Those days were long gone. The place remained, yet the people inside changed. My family were no longer with me. I lived alone."
    n_adv "I’ve thought about moving out before, but…"
    n_adv "I tilted my umbrella and stared at the dilapidated roof, emotions swirling in my chest. This apartment…was the last remnant of my family’s memories."
    n_adv "Too uneasy to stay, yet too wistful to part."
    Takumi "\"Haha...\""
    n_adv "I chuckled weakly. Even as I wallowed in this dilemma, my life continued on in perpetuity."
    n_adv "Stepping towards the door, I pulled out my keys."
    
    stop ambient fadeout 1.0
    scene black
    with fade
    play se1 "door_open"
    play ambient "longrain" fadein 1.0

    n_adv "{i}Click{/i}"

    scene bg takumi_inside
    with fade

    n_adv "A familiar dark corridor opened up before me, beckoning me into its solitary darkness once more, as it had always done countless times before."
    Takumi "\"...One day.\""
    n_adv "One day, perhaps the winds of change will arrive. Until then..."
    
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    stop se1 fadeout 1.0
    scene black
    with fade
    play se1 "door_open"

    n_adv "{i}Click{/i}"
    n_adv "I shut the door behind me."

    pause 2.0

label ch5: 
    python:
        set_info_scene("05")
        set_info_location("06")
        set_info_date(10, "Sep", "thu")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg bridge_night
    show rain_particle
    with fade
    play ambient "rain" fadein 2.0 volume 0.50
    play music audio.rainfall fadein 1.0
    
    $ show_date()

    n_adv "…Why? Why did they throw away their life? I pondered as red lights flashed all around me."
    n_adv "Standing under the callous rain, my legs remained rooted in place. Droplets of rainwater slid off my hair, creating ripples as they fell to the ground. In front of my eyes…lay the scene of the terrible accident."
    n_adv "The sedan had crashed into the police cruiser at full speed. It combusted almost instantaneously, despite the heavy rain. The resulting fire was too intense and suffocating for anyone to attempt an immediate rescue."
    n_adv "As the rain battered on my shoulders, I desperately hoped for a miracle to occur for the driver to escape alive."
    n_adv "By the time the sirens of the paramedics arrived, I finally realized how naive my lingering hope was."
    n_adv "I felt terrible. This isn’t what I wanted."
    Hiraku "\"I’m sorry…\""
    n_adv "I whispered to no one in particular. Even if the driver’s soul could hear me, I’m sure I had no right to be forgiven. No matter what kind of person they were, the loss of a life wasn’t something that could be justified by human laws."
    n_adv "I could only watch in silence, cursing my own powerlessness as the firefighters extinguished the flame. By then, all that remained inside was a corpse burnt beyond recognition."
    n_adv "..."
    n_adv "There’s nothing to be accomplished by beating myself up any further."
    Hiraku "\"Ah...\""
    n_adv "I finally noticed how much my body was shivering. Wrapping my arms around my chest, I scanned the personnel on scene. I spotted a senior-looking officer calmly instructing the paramedics. With unsteady legs, approached him."
    n_adv "Despite my years in this profession, I was inexperienced in dealing with deaths."
    S_Officer "\"You’re...the one from Kita Ward, correct—\""
    n_adv "He paused for a second to recall my name."
    S_Officer "\"Officer Inoue?\""
    Hiraku "\"Yes.\""
    n_adv "I was startled at how weak my voice sounded."
    Hiraku "\"What can I do to help?\""
    n_adv "He sized me up for a second."
    S_Officer "\"It’s ok, you can go back and report to your supervisor. We’ll handle the scene over here.\""
    n_adv "He refused the offer."
    Hiraku "\"But sir, I can also help.\""
    n_adv "I was adamant, desperate to get a chance to atone for my mistake in any way."
    S_Officer "\"I said just go home. You’re clearly in no shape to help.\""
    n_adv "Realizing how harsh that sounded, he added while scratching his head."
    S_Officer "\"What I mean is, I’ve been through your experience. I know how traumatizing it can be. Don’t push yourself.\""
    Hiraku "\"But...\""
    n_adv "I was at a loss for words for a moment. Was I so shaken that even a stranger could tell? In the end, I decided to swallow it in."
    Hiraku "\"Yes, sir. Thank you…very much.\""
    n_adv "I replied hesitantly."
    n_adv "It didn’t sit right with me, but maybe he wasn’t completely wrong. I needed to sort through my feelings. Exchanging salutes, I returned to my car, completely soaked to the bone."
    
    scene bg car_night_rain
    with fade
    play ambient "rain_inside_car" fadein 2.0 volume 0.25

    python:
        set_info_location("04")

    n_adv "The ride back to the police HQ was one in silence. All the while, the same question repeated itself in my mind."
    Hiraku "\"...Why?\""
    n_adv "Abandoning their own life like that… I couldn’t wrap my head around it. Was there something wrong with the driver? Was there something wrong with me for not understanding?"
    n_adv "I couldn’t understand. It all seemed so bizarre to me."
    Hiraku "\"What should I do? What…can I do?\""
    n_adv "I was lost."
    n_adv "My fingers subconsciously drifted towards the police badge attached to my vest. I gently wrapped it inside my palm."
    
    stop ambient fadeout 2.0
    
    Hiraku "\"Nee-san...\""
    
    scene placeholder
    with fade 
    
    n_adv "You always knew what to do in every situation. If only you were here, I’m sure you would be able to guide me…"
    n_adv "Tears threatened to drip from my eyes. Seven years later, and I still miss you so much."
    
    scene bg car_night_rain
    with fade
    play ambient "rain_inside_car" fadein 2.0 volume 0.25
    
    n_adv "..."
    Hiraku "\"Stop...\""
    n_adv "I whispered to myself, wiping the tears away. I promised I’d stop relying on you, didn’t I? When will I learn…that I need to be independent?"
    Hiraku "\"{i}Sigh...{i}\""
    n_adv "I gripped the steering wheel tightly. Guilt welled up within me. For taking a life. For abandoning the scene. For fleeing from my responsibility."
    n_adv "But more than anything else…for the fact that I could shed a tear for my sister, after all these years, yet not for the life I just took with my bare hands."
    n_adv "Within this suffocating space, only the bite of the cold provided any distraction, a sensation I welcomed. It was nothing compared to what I deserved, but even if just a tiny bit…"
    Hiraku "\"...\""
    
    stop ambient fadeout 2.0
    stop music fadeout 1.0
    scene black 
    with fade
    
    n_adv "The ride continued in silence as my inner turmoil ate away at my mind."

    pause 2.0

label ch6:
    python:
        set_info_scene("06")
        set_info_location("11")
        set_info_date(10, "Sep", "thu")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg airin_night
    show rain_particle
    with fade
    play ambient "lightrain" fadein 2.0
    play music audio.osmanthus fadein 1.0
    
    $ show_date()

    n_adv "Between the dim lights of sparsely placed lampposts, my steps rang alongside the clatter of rain. Holding my umbrella low, I tried to keep my fresh pair of trousers dry, although that was quickly proving to be an impossible task."
    n_adv "There was hardly anybody outside, and those I encountered were either the homeless seeking shelter under shallow eaves or drunkards with far more alcohol in their bodies than common sense."
    n_adv "Avoiding eye contact, I strode along the street briskly. My destination lay somewhere in the outskirts of the area, in an even more remote part of the district."
    
    scene bg a_alleyway
    show rain_particle
    with fade
    
    python:
        set_info_location("12")

    n_adv "Earlier, I arrived home only to find that I had forgotten to restock on food. Coincidentally, I happened to find a discount coupon slipped under my apartment door. It was for a bar I knew well and occasionally visited."
    Takumi "\"Well, can’t hurt to treat myself once in a while, right?\""
    n_adv "And if I had to eat outside anyway, why not a place I was familiar with? With that feeble justification, I had set out on my way."
    n_adv "Although, now that I was actually here, I was starting to have second thoughts. The empty alleyways leading to the bar had always been a little shady, but under the veil of rain, it felt even more…isolated than usual."
    n_adv "Passing by another homeless person sleeping on the floor, I tucked my head low and hastened my pace. I was even beginning to doubt whether I was going the right way."
    
    scene bg z_bar outside
    show rain_particle
    with fade 

    Takumi "\"Ah…there it is.\""
    n_adv "After a couple more uncertain turns, I finally spotted the bar. An odd metal door on an otherwise unassuming wall, accompanied by a plain wooden signboard."
    n_adv "Shallow overhanging eaves protected it from the rain. A lone ceiling lamp dangled from above, occasionally flickering."
    n_adv "Inconspicuous as it was, it still stood out from the depressing atmosphere of the street."
    n_adv "I breathed out a sigh of relief. This was undoubtedly the place. It had such a suspicious appearance, no one would’ve imagined it actually housed a bar."
    n_adv "I chuckled to myself. I remember the first time I found out, I..."
    Takumi "\"Huh...\""
    n_adv "Wait…what was I chuckling for again? I couldn’t quite remember when and how I found out."
    n_adv "..."
    n_adv "My memory must’ve been getting fuzzier from all the stress from work. Oh well, it’s nothing new. I brushed it away before approaching the door. The handle was cold to the touch from the damp air."
    
    stop ambient fadeout 1.0
    scene bg z_bar_entrance
    play ambient "longrain" fadein 1.0
    play se1 "door_jingle"
    
    python:
        set_info_location("13")

    n_adv "A tiny entrance greeted me. It was a small, bare-walled room, decorated with several canvases of antique paintings. Warm incandescent lights hung from the ceiling, highlighting the thin layer of dust on the frames."
    n_adv "Directly in front of me was a narrow twisting staircase leading underground. You couldn’t see where it led to from up here."
    n_adv "If that doesn’t look suspicious, I don’t know what does. I shook my head lightly. How this bar manages to keep running was beyond me."
    n_adv "Next to the doorframe, a black bin was provided to hold umbrellas. I placed mine inside. Before continuing any further, I took my phone out and added a line to my notes."
    Takumi "\"Went to the bar at 19:20... There\""
    
    scene black
    with fade

    n_adv "My footsteps rang on the metal steps as I descended the stairs."
    
    play se1 "metal_stairs" fadein 1.0
    
    n_adv "{size=15}Clank...{/size}{size=20}Clank...{/size}{size=30}Clank.{/size}"
    
    stop music fadeout 2.0
    stop se1 fadeout 3.0
    
    n_adv "The staircase continued for nearly two stories. Halfway through, I could make out a faint but distinct melody of piano keys from below."
    
    stop ambient fadeout 1.0
    play ambient "Clair_de_Lune" fadein 15.0
    
    n_adv "A pleasant fragrance of musty wood like you’d find in a library tickled my nose. After several turns, a spacious room with atmospheric lighting opened before me."
    noname_adv "\"Welcome to my humble establishment, dear customer.\""
    n_adv "A deep, pleasant voice addressed me."
    
    scene bg piano_scene
    with fade

    n_adv "The voice belonged to none other than the man playing the piano. Even as he greeted me, he made no motions to leave the seat. Instead, the piece continued on as his visage subtly swayed alongside the tune."
    n_adv "His face wore a serene expression, his eyes lost in a distant world. His fingers flowed through the keys effortlessly, creating beautiful melodies with each passing stroke."
    n_adv "Enraptured by the sight, my feet slowed to a halt. I couldn’t find it within me to reply and disturb the moment."
    n_adv "I remained motionless, captivated by the tranquility of the scene. For a while, everything was frozen in place, save for the man’s elegant movements."
    n_adv "..."
    n_adv "..."
    n_adv "..."
    
    stop ambient fadeout 5.0

    n_adv "Alas, all good things must come to an end. Eventually, the final note was struck, and the hum of the melody faded from the air. He rose up and softly closed the piano lid."
    
    scene bg bar_inside_lounge
    with fade
    play se1 "gear_shift"
    play music audio.night fadein 2.0

    n_adv "Only then did he turn to look at me."
    TBD "\"Well, if it isn’t Ito…Takumi-sama. I hope you enjoyed my performance.\""
    Takumi "\"That was…simply breathtaking, TBD-san.\""
    TBD "\"Haha, I’m glad to hear that.\""
    n_adv "Broken from my trance, I finally took in my surroundings."
    n_adv "Beneath the facade of the entrance, it was a proper and well-maintained establishment. Hanging pot plants and grapevines adorned the ceiling."
    n_adv "Several velvet sofas were arranged around the room nonuniformly, creating a perfect blend of comfort and style."
    Takumi "\"The bar, too, looks amazing as usual.\""
    TBD "\"Thank you. I take pride in maintaining this place.\""
    n_adv "He circled around the room and into the centerpiece of the bar."
    
    scene bg bar_inside
    with fade 

    n_adv "A rustic and polished wooden bar with glossy countertop, decked in rows and rows of liquor racks attached to the wall. And of course, it wouldn’t be complete without the bartender, claiming his place behind the counter."
    TBD "\"Please, have a seat.\""
    n_adv "The bartender smiled warmly as he gestured towards one of the stools. I took him up on the offer. There were no other customers, but that had always been the case every time I visited, so I paid it no mind."
    Takumi "\"How long have you been playing the piano for?\""
    TBD "\"Hmm, I’m not quite sure, truth be told. It was a long time ago.\""
    Takumi "\"I’ve never seen you play before. Do you play often?\""
    TBD "\"Not terribly. Only whenever the mood calls for it.\""
    Takumi "\"Ah.\""
    TBD "\"But enough about me. Did you perchance weather through the rain getting here, Takumi-sama?\""
    n_adv "I smiled exasperatedly at his eccentric manner of addressing people. By now, I was used to it."
    Takumi "\"I did. Got my trousers all wet too, but it’s worth it.\""
    TBD "\"Haha, you look a little tired as well. Busy work today?\""
    n_adv "He pulled out a leatherback menu book from under the counter and handed it to me."
    Takumi "\"Ah, you could tell? It’s half that — and also having to sit on the train with soaked pants. That was…not pleasant.\""
    TBD "\"That sounds awful. What happened?\""
    Takumi "\"Some driver decided they wanted to be a jackass and sped through a puddle of water. I happened to be in the line of fire.\""
    TBD "\"That’s unfortunate. Some people shouldn’t be allowed behind the steering wheels.\""
    Takumi "\"Right?\""
    n_adv "As we chatted, I browsed through the menu."
    Takumi "\"Any new additions, by the way?\""
    TBD "\"Same old, I’m afraid. I may, however, give recommendations on dishes you haven’t tried.\""
    Takumi "\"Sounds good, give me one.\""
    TBD "\"Hmm…\""
    n_adv "He flipped through several pages of the menu and landed on one."
    TBD "\"How does a black pepper beef stew sound? It’s a hearty meal perfect to warm up the body.\""
    Takumi "\"Oh, I haven’t had one in a while. I’ll have that then.\""
    TBD "\"Certainly. Any drinks to pair with it?\""
    Takumi "\"Hmm… I’ll just follow your recommendation again.\""
    TBD "\"Some brown ale would pair well with the stew.\""
    Takumi "\"That’s the one, then.\""
    TBD "\"Certainly. Please wait for fifteen minutes.\""
    n_adv "He disappeared into the back corridor."
    n_adv "I clasped the menu shut and set it on the counter. With nothing else to do, I let my eyes wander around the room."
    
    scene bg bar_inside_lounge
    with fade
    
    n_adv "Near the back, a wooden billboard table was set up under a large spotlight. And just behind that, a vintage gramophone set in the corner, the vinyl disc inside spinning. The whole room radiated rusticness and coziness."
    
    stop music fadeout 5.0

    n_adv "It’s so comforting, I could almost fall asleep. In fact, my eyelids were getting heavier by the second…"
    
    scene black
    with white3

    n_adv "..."

    scene bg bar_inside
    with white3
    play music audio.night fadein 5.0

    TBD "\"Takumi-sama? The meal is ready.\""
    Takumi "\"A—ah, sorry. I almost fell asleep. Just a little tired.\""
    TBD "\"Haha, I’ll take that as a compliment.\""
    n_adv "He set down a steaming platter of stew on the counter. The savory smell entered my nose, rousing me from the drowsiness."
    
    scene bg food_soup
    with fade

    Takumi "\"Ooh, this looks amazing.\""
    TBD "\"It uses high quality beef, simmered in my house blend of spices.\""
    n_adv "He proudly explained while filling a pint glass."
    
    play se1 "glass_clink"

    TBD "\"Here, your brown ale.\""
    Takumi "\"Thanks for the meal.\""
    n_adv "I grabbed the utensils and took the first bite."
    Takumi "\"Mmf.\""
    n_adv "The warmth and juiciness of the meat permeated my mouth. Flavor burst out of the sauce, wrapping my tongue in a sweet-savory sensation." 
    n_adv "A little strong, but just perfect for this cold weather. As I swallowed, the warmth spread throughout my stomach, rejuvenating my whole body."
    
    scene bg bar_inside
    with fade

    TBD "\"Is the taste to your liking?\""
    Takumi "\"It’s, mmf, amazing as usual.\""
    n_adv "I replied with a mouthful of food."
    TBD "\"I’m glad my cooking still stands up to your standards.\""
    Takumi "\"Wait, you’re the cook as well?\""
    TBD "\"I am the only staff member in this establishment.\""
    Takumi "\"Oh wow… That reminds me, something’s been on my mind for a while now.\""
    n_adv "He waited for me to continue."
    Takumi "\"How do you manage to keep this bar running? Sorry if it sounds rude, but I’ve never seen any other customers here.\""
    n_adv "He chuckled heartily."
    TBD "\"Well, let’s just say I have a side business that allows me to run this bar as a hobby.\""
    n_adv "My curiosity was piqued."
    Takumi "\"Really? What kind of business is it?\""
    TBD "\"Haha, let’s just call it a secret of the trade.\""
    Takumi "\"I see…\""
    n_adv "If he had a reason to hide it, then I shouldn’t pry further."
    Takumi "\"Either way, your food is amazing. My mom used to make this all the time, and my brother loved it.\""
    n_adv "I scooped a mouthful of piping hot potato chunk."
    TBD "\"You have a brother? What is he like?\""
    Takumi "\"Yeah, a twin brother. We…separated a few years ago, so I don’t know where he is or what he’s like right now.\""
    TBD "\"Ah… I’m sorry to hear that.\""
    n_adv "His eyes showed genuine interest, yet he stayed silent to let me decide if I wanted to continue."
    
    stop music fadeout 2.0

    Takumi "\"...\""
    
    play music audio.distant fadein 3.0

    Takumi "\"He…was born slightly later. Technically, that makes me the older brother.\""
    TBD "\"I see.\""
    Takumi "\"You know, we looked so alike even our mother mistook us often.\""
    TBD "\"That sounds fun.\""
    Takumi "\"It was. We pulled pranks on her all the time.\""
    TBD "\"Haha, she must’ve been annoyed.\""
    Takumi "\"Oh, she was, every time. Haha…\""
    n_adv "How long ago was that? My eyes drifted away into the distant past."
    Takumi "\"...Our family wasn’t rich, but we weren’t struggling either. Our mother was home often. We played with the neighbor kids often. It was a normal, but very fun childhood.\""
    TBD "\"That sounds like a good family. What’s his name?\""
    n_adv "My fingers froze in place. My chest tightened."
    Takumi "\"...\""
    TBD "\"Ah, It’s completely fine if you wish to not say. I was simply wond—\""
    Takumi "\"No, that’s not it. It’s just that…\""
    TBD "\"...?\""
    Takumi "\"...I don’t know his name.\""
    n_adv "I hung my head in shame."
    TBD "\"...\""
    n_adv "He was speechless for a moment. My lips twisted into a smile of self-derision."
    n_adv "Right, that is the proper reaction, isn’t it?"
    TBD "\"My apologies. I didn’t mean to delve into sensitive circumstances.\""
    Takumi "\"It’s alright.\""
    n_adv "I took a deep breath and continued."
    Takumi "\"Our lives passed on normally…up until one day, however many years ago that was. Something…happened.\""
    n_adv "My words stuck in my throat. Even after all these years, accepting it…was still difficult."
    Takumi "\"...My memory of it is foggy. I can’t remember what happened, but our mother died abruptly.\""
    TBD "\"...My condolences.\""
    
    stop music fadeout 2.0
    $ nvl_mod = True
    
    scene black
    with fade
    pause 1.0
    
    scene bg funeral
    with fade

    nvl show
    n_nvl "At her funeral, my brother stood right beside me and comforted me. Despite being younger, he had always been the more mature of us twins."
    
    scene bg funeral
    with dissolve

    n_nvl "As people slowly drifted away, we were the only two remaining ones after the procession ended."
    ▊▊▊▊▊ "\"It’s gonna be ok, Takumi.\""
    t_nvl "\"Mm…\""  
    nvl clear

    nvl show
    ▊▊▊▊▊ "\"We’re still here. Both of us.\""
    n_nvl "Our father passed away before we were born, and we had no family left to adopt us. They put us in separate orphanages."
    n_nvl "At first, I was allowed to visit him once a week. And then…once a month. Until…"
    
    scene bg funeral
    with dissolve

    n_nvl "One day, I wasn’t allowed to visit him anymore. I protested and protested, but to no avail. From that day onwards, I would never see him anymore. He had drifted away from my reach."
    t_nvl "\"▊▊▊▊▊…\""
    
    scene black
    with fade

    n_nvl "Over the years, memories of him began to drift away."
    nvl clear
    nvl hide

    scene bg bar_inside
    with fade
    $ nvl_mod = False
    play music audio.distant fadein 2.0

    Takumi "\"Day after day, I was forced to continue living apart from my brother, all while memories of him slowly slipped away from me.\""
    TBD "\"...\""
    Takumi "\"And then one day…even his name finally escaped my grasp. I don’t even know if he’s alive.\""
    n_adv "Tears threatened to drop, my voice quivering."
    Takumi "\"I’m a horrible brother, aren’t I?\""
    TBD "\"...Takumi-sama, I’m certain that was no fault of yours. Separating a child from their sibling… that’s despicable.\""
    n_adv "TBD hung his head."
    TBD "\"Unfortunately, there is nothing I can do but listen to your worries.\""
    Takumi "\"That’s plenty, TBD-san. That is plenty.\""
    Takumi "\"{i}-hic-{/i}\""
    n_adv "It was getting pretty late, and the alcohol was starting to hit. I wiped the tears away from my eyes and finished the rest of my meal in silence. Perhaps it was just my imagination, but after that, more than ever, the stew tasted just like home."
    n_adv "With each spoonful I chewed, I could picture myself sitting at the family dinner table, alongside my mother and brother, enjoying a warm family dinner. And strangely, for the whole duration, my eyes would not stop getting blurry."
    
    stop music fadeout 2.0

    n_adv "…"

    play music audio.night fadein 2.0

    Takumi "\"Thank you for the meal, and for listening to me earlier.\""
    TBD "\"...No, thank you for telling your story. I could not imagine how hard a burden that was on your chest.\""
    Takumi "\"You were a good listener, TBD. I’m glad I {i}-hic-{/i} came here today.\""
    TBD "\"The pleasure is all mine.\""
    n_adv "Part of me was reluctant to leave, but I was afraid… Afraid that if I stayed to continue my reminiscence, the emotions might be too much to handle. Slowly, I stood up, wiped my eyes dry, and was about to pay the bill."
    TBD "\"There is no need, Takumi-sama. Today, it’s on the house.\""
    Takumi "\"But, I can’t—\""
    TBD "\"It’s okay. Consider it as thanks for telling your story.\""
    n_adv "He extended a hand to gesture that it was okay."
    Takumi "\"...Thank you. Goodbye for today, then.\""
    n_adv "As I began to ascend the stairs, his voice rang from behind."
    TBD "\"...Don’t give up.\"" 
    Takumi "\"...?\""
    TBD "\"I’m certain, he’s out there somewhere, still alive and doing well.\""
    Takumi "\"...Yeah, thank you.\""
    n_adv "I smiled weakly at his encouragement. With a goodbye wave, the bartender sent me off."
    TBD "\"Thank you for coming today. I will be waiting for your next visit, perhaps with another piano piece.\""
    Takumi "\"Yeah, until next time.\""
    
    stop music fadeout 2.0
    
    scene bg z_bar_entrance
    with fade 
    play se1 "door_jingle"
    $ renpy.pause(2.0, hard=True)

    scene bg z_bar outside
    show rain_particle
    with fade
    play ambient "rain" fadein 2.0
    
    n_adv "The rain hadn’t let up even a tiny bit. I stood under the eaves and peered into the gloomy sky."
    n_adv "Where could you be right now, my long-lost brother? Are we facing the same rainy sky at this very moment? For a little while, I pictured him standing under the rain, staring at the sky and wondering the same about me."
    n_adv "And then I unfurled the umbrella and walked on my way."
    
    stop ambient fadeout 2.0
    scene black
    with fade
    pause 2.0

label ch7:
    python:
        set_info_scene("07")
        set_info_location("13")
        set_info_date(10, "Sep", "thu")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg bar_inside_lounge
    with fade
    play music audio.meeting fadein 2.0

    $ show_date()

    noname_adv "\"Why didn’t you tell him?\""
    n_adv "A frail, raspy voice resounded from the back of the lounge. Right against the wall sat a majestic gold-framed sofa, larger and more comfortable than the rest."
    n_adv "It looked more like a throne than anything else. And sat inside it was...nothing. Yet, a presence was definitely there."
    TBD "\"You saw how it went last time. It’s too early.\""
    noname_adv "\"Heh. You’re afraid, even with the insurance?\""
    n_adv "Picking up on a hint of mockery in the phantom’s voice, the bartender grimaced but refrained from replying."
    noname_adv "\"Well, do whatever you want.\""
    TBD "\"Always had been my intention.\""
    noname_adv "\"And fail, like you always do.\""
    n_adv "Those words bore a tinge of resentment."
    TBD "\"...\""
    n_adv "He held his tongue once more. The last thing he wanted was to give the phantom the satisfaction of getting under his skin."
    noname_adv "\"Anyway, looks like it’s about time. I’ll leave you to deal with it. Let’s see just how good this insurance you keep talking about is.\""
    n_adv "A small gust of wind churned inside the room, ruffling his hair. A moment later, the presence could no longer be felt. Vanished, alongside the dispersal of the gust."
    n_adv "The bartender sighed tiredly and drifted his eyes downwards, onto a monitor set up underneath the counter."
   
    scene bg cctv
    with fade

    n_adv "He scanned each of the boxes displayed for any movement."
    TBD "\"...!\""
    n_adv "His eyes halted and lingered on one spot. Like clockwork, they’ve arrived, exactly as he expected."
    n_adv "Uneasiness reflected in his eyes, he took out his flip phone and dialed a number."
    
    stop music fadeout 2.0
    scene black
    with fade
    pause 2.0

label ch8:
    python:
        set_info_scene("08")
        set_info_location("14")
        set_info_date(11, "Sep", "fri")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg police_office
    with fade

    $ show_date()

    Supervisor "\"So, only those guys from Yodogawa are there right now?\""
    Hiraku "\"Yes, sir.\""

    play se1 "footstep" fadein 2.0

    Supervisor "\"Those sly bastards. I bet they’re just trying to take all the credit for themselves.\""
    n_adv "He paced around the room."
    Supervisor "\"Well, what’s done is done. You still need to write your own report. Just put in whatever detail you know and submit it by tomorrow at the latest.\""
    Hiraku "\"Yes, sir.\""
    n_adv "That was all I could reply with."
    n_adv "..."

    scene bg police_office
    with fade 
    play music audio.rainfall fadein 2.0
    play ambient "crowd_inside" fadein 2.0 volume 0.5

    n_adv "I stared at the plain, white wall absentmindedly. Occasionally, the minute hand on the clock ticked away. They had never felt as excruciatingly slow." 
    n_adv "Murmurs and clicking sounds from my coworkers filled the room, but they served as little more than background noise."
    n_adv "My fingers rested on the computer keyboard, motionless. The text cursor blinked repeatedly on the computer screen, awaiting further input."
    Hiraku "\"{i}Sigh.{/i}\""
    n_adv "Even after a warm shower and a fresh set of clothes, my body remained listless. I hadn’t moved from my desk for at least half an hour now."
    n_adv "The report was submitted long ago, but my mind refused to leave the crime scene. I pictured it over and over, replaying the very last moment as the car collided, like a broken cassette tape."
    n_adv "I wondered, what was going through the driver’s mind within that last moment?"
    Hiraku "\"...\""
    n_adv "I didn’t know if I agreed with my supervisor’s words, but I was definitely regretting backing out so easily. Even now, I was contemplating driving back to the scene."
    Hiraku "\"And then what, run again?\""
    n_adv "I chuckled in self-derision. These pristine white walls that I used to admire so much now seemed suffocating."
    
    stop ambient fadeout 1.0
    play ambient "phone_vibrate"

    n_adv "{i}Bzzt, bzzt.{/i}"
    n_adv "It came from my phone on the desk. I'd put it on silence mode earlier. I wasn’t in a mood to answer calls, but at the same time, it could be something important."
    n_adv "Hesitantly, I picked it up and peered at the caller id."
    
    stop ambient
    stop music fadeout 1.0

    Hiraku "\"...?\""
    n_adv "An unidentified number was displayed. This was my work-issued phone, and I do occasionally get unidentified calls when I was assigned with people I’ve never met. However, my supervisor hadn’t mentioned anything this time."
    n_adv "My curiosity was piqued. For an inexplicable reason, I had a feeling that I wouldn’t want my coworkers to overhear. I switched the computer to sleep mode, then grabbed the phone and walked outside."
    
    scene bg white_corridor
    with fade
    pause 2.0

    scene bg plain_room
    with fade
    pause 2.0
    
    scene bg police_office
    with fade

    n_adv "Sitting on a bench, I clicked on the accept button and held my breath."
    Hiraku "\"...\""
    
    play music audio.suspicious fadein 2.0

    Phone "\"Hello, is this Officer Inoue?\""
    n_adv "A deep voice spoke from the other side."
    Hiraku "\"Who is this?\""
    Phone "\"That's not important right now.\""
    n_adv "What..? I racked my brain in an attempt to put a name to the voice, to no avail."
    Hiraku "\"...I won't listen to anything you have to say if you won't even tell me your name.\""
    n_adv "Everything that went through this phone was recorded. All I needed to do was goad him to talk."
    Phone "\"There is no time for this. A crime is about to happen.\""
    Hiraku "\"...!\""
    Phone "\"Someone is about to fall victim to yakuza aggression, perhaps even resulting in death.\""
    n_adv "The yakuza? Things had been relatively quiet with them recently. The public loved to romanticize and blame them for every small incident. Could it be a prank call?"
    n_adv "…No, the average person wouldn't have been able to get this number."
    Hiraku "\"How do I know you're telling the truth?\""
    Phone "\"I will send you a location. You can find out yourself.\""
    Hiraku "\"Tsk, quit bullshitting me.\""
    n_adv "Alarm bells rang in my mind. What exactly was this man’s intentions?"
    Phone "\"I am telling the truth.\""
    n_adv "Just who was this guy anyway? I paced around the room, trying my damndest to recall every single acquaintance with the same type of voice."
    n_adv "…It’s useless! No one came to mind."
    Hiraku "\"Why didn't you call the police station instead? Why did you— Where did you get this number from in the first place?\""
    n_adv "I tapped my shoes in irritation. Why was this happening now, of all times?"
    Phone "\"...I have reasons which I can't disclose.\""
    Hiraku "\"You’re being extremely suspicious right now, you know that right? If you're really telling the truth, give me a reason to believe you!\""
    n_adv "Gah, my voice raised by accident. I covered my mouth, hoping that no one else heard that."
    Phone "\"Inoue-san, I guarantee an explanation at a later date. For now, you have to believe me.\""
    Hiraku "\"I’m hanging up!\""
    n_adv "I hovered my finger above the end call button."
    Phone "\"Inoue-san!\""
    n_adv "His voice became tense."
    Phone "\"Aren’t you a police officer? Are you about to abandon someone’s life out of doubt!?\""
    n_adv "Just press it. He’s speaking nonsense."
    n_adv "..."
    n_adv "But I couldn’t. My finger froze in place, unable to close the last remaining gap. Something at the back of my mind was nagging that ignoring his words would be a terrible mistake."
    n_adv "\"Abandon someone’s life\". His words echoed in my mind."
    n_adv "What if — just what if — he was telling the truth? If there was a one in a million chance he wasn’t lying…"
    Phone "{size=20}\"Inoue-san!\"{/size}"
    n_adv "His voice faded into the background as I fell into deep thought. What should I do? It’s probably fake, but on the off chance it’s real…"
    n_adv "Could it be a trap!? There’s no reason someone would want to harm me…was there? What’s the right move?"
    n_adv "Anxiety began to crawl over me. Beads of sweat formed on my face. The shadows looming over the corners of this cramped room began to close in, encasing me in a prison of doubt."
    n_adv "..."
    Phone "\"Inoue-san!\""
    n_adv "His pleading voice snapped me back to reality."
    Hiraku "\"Gh...\""
    n_adv "Take a deep breath, Hiraku. Take a deep breath."
    
    stop music fadeout 2.0

    Hiraku "\"{i}Inhale… Exhale…{i}\""
    n_adv "..."

    play music audio.answer

    n_adv "Was it fake? Likely. A trap? Possibly. But after what happened today…do I even have the right to refuse? If another person dies because of me, I…"
    n_adv "That’s…that’s too much to bear. I can’t let that happen."
    n_adv "As my mind cleared, the answer presented itself, clear as day. It might not be enough for atonement, but…I have to take this chance."
    n_adv "It’s as simple as that, wasn’t it? What did I even hesitate for? After all, this was the path I pursued, wasn’t it?"
    
    scene placeholder
    with fade 

    Hiraku "\"...\""
    
    scene bg police_office
    with fade

    n_adv "Pushing all doubts to the back of my mind, I made my decision."
    
    Hiraku "\"Fine… I’ll trust you.\""
    n_adv "A breath of relief came from the other side."
    Phone "\"Thank you, Inoue-san. You need to hurry, there isn’t much time left.\""
    n_adv "I rose to my feet and strode for the door, my steps firm. As it swung open, lights flooded my eyes once more."
    
    scene bg white_corridor
    with fade
    pause 2.0

    scene bg police_office
    with fade

    n_adv "I rushed towards the lobby, past my coworkers’ questioning glances."
    Supervisor "\"Inoue-san? Where are you—\""
    Hiraku "\"Sorry, chief! I’ll explain later!\""
    
    scene bg police_lounge
    with fade
    play ambient "longrain" fadein 0.5

    n_adv "To the parking lot—"
    
    scene bg parking_lot
    with fade
    play ambient "lightrain" fadein 0.5

    n_adv "—and into my car."
    
    play ambient "rain_inside_car" fadein 0.5 volume 0.25

    python:
        set_info_location("04")
    n_adv "A new message popped up. It was an image sent by the unknown caller."
    Hiraku "\"...!\""
    n_adv "I recognized the place. Placing the phone down, I turned on the ignition."
    Phone "\"I pray that you will make it in time.\""
    Hiraku "\"Ten minutes. Just hold out for ten minutes.\""
    n_adv "No rest for the weary. Whatever lies ahead, I’ll face it head-on."
    
    play se1 "car_rev"
    stop ambient fadeout 2.0
    stop music fadeout 2.0

    scene black
    with fade
    pause 2.0

label ch9:
    python:
        set_info_scene("09")
        set_info_location("15")
        set_info_date(11, "Sep", "fri")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg atm_close
    show rain_particle
    with fade
    play music audio.cold fadein 2.0
    play ambient "lightrain" fadein 1.0
    play se1 "atm"

    $ show_date()

    n_adv "{i}Clack clack clack.{i}"    
    n_adv "A faint rhythm of clicking buttons entered my ears, breaking the monotony of the rain. It came from the lone ATM machine in front of me, sheltered under a flimsy roof. Another person was currently using it, with me waiting behind for my turn."
    
    stop se1

    n_adv "Rats scurried along the sidewalks, casting shadows onto the ground. Puddles filled with scraps of trash lined the edge of the gutters. The dying bulbs in the lampposts flickered uncertainly. "
    Takumi "\"{i}-hic-{/i}\""
    n_adv "The hiccup caused me to stumble, stepping on a pebble and nearly losing my balance."
    Takumi "\"Whew...\""
    n_adv "That was close. I almost lost my grip on the umbrella."
    n_adv "A tinge of worry crept into my mind. How long was this guy going to take? The alcohol was starting to kick in. The sooner I could get out of here, the better."
    n_adv "I looked around the dark, empty alleyway. There was no other person in sight aside from the two of us. Uneasiness began to crawl up my skin. Should I leave now after all?"
    n_adv "Just as I was wondering, the machine whirred, signaling the completion of the process. Finally. I stepped forwards."
    
    stop music fadeout 2.0
    scene bg atm_far
    show rain_particle
    with fade
    
    n_adv "As the person ahead turned around, he made eye contact with me."
    
    play music audio.fear fadein 1.0

    U_Man "\"Genji!?\""
    Takumi "\"...?\""
    n_adv "Caught off-guard, I glanced behind, but there was no one. Was this person talking to ...me?"
    Takumi "\"Um...\""
    U_Man "\"Kheh, you have some guts showing your face again around here.\""
    n_adv "His voice was shrill and nasal, his lips twisting into a wicked grin."
    n_adv "From behind and through the rain, he looked like an average guy. However, looking from upfront and close nearly made me flinch. His eyes were as sharp as a razor, and his leather jacket couldn’t hide the lean physique underneath."
    n_adv "He stepped forward threateningly, his shoe grazing against the soil. As he moved, I noticed something on his neck skin peeking out underneath his shirt collar."
    Takumi "\"!!!\""
    n_adv "It was the outline of a tattoo!"
    n_adv "A tattoo was the symbol of a yakuza member. It instantly sobered me up. I threw both hands in the air, the umbrella clattering to the ground."
    Takumi "\"Wait! Wait! You have the wrong guy!\""
    n_adv "I staggered backwards, my mind panicking. The man roared in laughter."
    U_Man "\"Really? You think that’ll work?\""
    n_adv "He matched my pace in unhurried steps, relishing in the fear reflected in my eyes. He paused right at the edge of the rain and tucked his arm inside his jacket folds."
    Takumi "\"!!!\""
    n_adv "Was it a weapon!? Was he grabbing a weapon!?"
    U_Man "\"Don’t move. This jacket is worth more than your scummy life.\""
    n_adv "He began to take off his jacket. Underneath, the tattoo traveled all the way to his forearms."
    n_adv "This was my chance! Breaking free of my daze, I sprinted away in a mad dash."
    
    scene bg a_alleyway
    show rain_particle
    with fade 
    play se1 "running_on_rain"

    n_adv "Anywhere was fine, as long as I could escape! Puddles splashed all over my trousers, but I couldn’t care less. I had to keep running!"
    n_adv "Was he chasing me? I glanced back for a split second, but the man hadn’t moved an inch from the ATM. I could make it out! Adrenaline pumping throughout my body, I didn’t dare slow down even a bit."
    n_adv "I didn’t know why he wasn’t chasing, but it’s a stroke of luck. The residential area wasn’t too far away now. Once I reach there, I could report—"
    
    play se1 "thud"

    n_adv "{i}Thud.{/i}"
    Takumi "\"Gh!?\""
    n_adv "While my head was turned, I bumped into someone. Thank god, another person!"
    Takumi "\"Help! Someone’s trying to kill me and...\""
    n_adv "My voice trailed off as I peered into the person I bumped into. It was a large, bald brute in a tank top." 
    n_adv "Right beside him was another man with even taller stature and just as intimidating. They stood unmoving, unbothered by the thunderstorm in the least."
    n_adv "My momentary relief was quickly snuffed, replaced by heightened fear. I staggered back several steps, my mouth agape in terror."
    n_adv "No… This can’t be happening! I was too afraid to utter another word."
    U_Man "\"I said ‘don’t move’, didn’t I?\""
    n_adv "I flinched as the shrill voice from earlier echoed from behind. I turned my head around."
    n_adv "His silhouette was leisurely approaching us. Under the crisscrossing dim lights, I could make out the same wicked grin on his face. In his right palm, I spotted the glint of a blade."
    Takumi "\"P-please! I swear I’m telling the truth! My name is Takumi, I can—\""
    T_Brute "\"Give it up, we know you have fake IDs.\""
    n_adv "The tall brute cut me off as the other folded my arms behind me. I tried to resist, but our strengths were leagues apart."
    Takumi "\"Agkhh!\""
    n_adv "My arms flared in pain."
    U_Man "\"Make sure you hold him tight. I’ve seen what this guy can do, he’s crazy strong.\""
    B_Brute "\"Right.\""
    n_adv "Spinning the knife around his wrist leisurely, he continued."
    U_Man "\"Do you know how hard we’ve been trying to find you? Our boss is gonna love this. I might even get a promotion, khahahaha!\""
    n_adv "He added, with a burst of shrill laughter."
    n_adv "I kept my eyes on the knife as it traced a slow arc straight to my neck. It grazed my hair and hovered there, almost touching my skin. One wrong move and I’d be dead."
    
    stop ambient fadeout 2.0
    play ambient "heartbeat"

    n_adv "{i}Ba-dump. Ba-dump. Ba-dump.{/i}"
    n_adv "I could hear my hammering heartbeat."
    
    stop ambient fadeout 2.0
    play ambient "lightrain" fadein 1.0
    Takumi "\"Hk...!\""
    n_adv "The blade touched my skin. I winced, imagining the worst."
    n_adv "..."
    n_adv "But it didn’t come. Fearfully, I peeled back my eyelids. The knife was still hovering over my neck. I stifled my ragged breathing to keep as much distance as possible from the blade."
    U_Man "\"Listen, we got some questions for you. You answer them nicely, and I’ll tell them to make your death quick. Otherwise...\""
    n_adv "He waved the knife in front of my face."
    U_Man "\"We have pleeeenty of torture methods, khahaha!\""
    Takumi "\"I-I swear, I don’t know what you’re talking ab—\""
    n_adv "The man stomped on the ground, causing me to flinch. He then brought the blade to my left cheek — drawing blood — and spoke coldly."
    U_Man "\"You still gonna keep up that act? Let me remind you who you’re dealing with.\""
    n_adv "He pulled his sleeves up, revealing a tattoo of an oriental dragon coiling around his upper arm."
    U_Man "\"Not that you don’t already know.\""
    n_adv "He spat those words out. Resting the blade against my neck once more, he continued."
    U_Man "\"Now, I’ll give you one last chance. Answer me. Who do you work for, Ito Genji?\""
    Takumi "\"...!\""
    
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    scene ito_genji
    with fade
    pause 3.0

    scene bg a_alleyway
    show rain_particle
    with fade
    play ambient "rain" fadein 1.0
    play music audio.fear fadein 2.0

    n_adv "..."
    n_adv "Only the sound of the pounding rain and my own breathing reached my ears. Trapped within this deadlock where no answer would save me, I could only pray for a miracle."
    
    stop music fadeout 1.0
    stop ambient fadeout 2.0
    scene black
    with fade 
    pause 2.0

label ch10:
    python:
        set_info_scene("10")
        set_info_location("15")
        set_info_date(11, "Sep", "fri")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg a_alleyway_corner
    show rain_particle
    with fade
    play ambient "rain" fadein 2.0
    play music audio.fear fadein 2.0

    $ show_date()

    n_adv "I was pressed against the edge of the wall, straining my ears for all sounds."
    U_Man "\"—Who do you work for, Ito Genji?\""
    n_adv "The rain muffled most of the voice. Even with my excellent hearing, I could barely pick it up."
    n_adv "My car was parked a small distance away. Earlier, I had been warned by the unknown caller to turn off the siren. Combined with the rain, they managed to hide the noise of the engine as I approached."
    n_adv "I had snuck up on foot the rest of the way. True enough, the scene that greeted me didn’t betray his claims. I leaned my head ever so slightly to take a peek."
    
    scene bg a_alleyway
    show rain_particle
    with fade 
    
    n_adv "…Four people. Three of them — including the victim — had their backs turned on me. The one who spoke earlier was facing this way, but he hadn’t noticed me yet."
    
    scene bg a_alleyway_corner
    show rain_particle
    with fade
    
    n_adv "I carefully retraced several steps backwards and took out my radio."
    Hiraku "\"This is Inoue Hiraku from Patrol Car 17, currently on foot. HQ, do you copy?\""
    n_adv "I spoke in a half-whisper."
    
    play se1 "static"

    Radio "\"Inoue-san, this is Tenma Station. What’s the matter?\""
    n_adv "The unknown caller might’ve wanted to keep this matter a secret, but to hell with that. The situation was a little too much for me to handle alone."
    Hiraku "\"There’s a heavy assault in progress. Three assailants and one victim. At least one of them is armed with a category M weapon. Can you send backup over to my location?\""
    n_adv "The radio went silent for several seconds."
    n_adv "..."
    Radio "\"Authorized. Sending two units and an ambulance to your location. Estimated arrival time is in ten minutes. The ambulance might take a little longer.\""
    Hiraku "\"Thanks. Also, please tell them to be discreet. They haven’t spotted me yet.\""
    Radio "\"Copy that. What’s the current status of the victim?\""
    Hiraku "\"Physical condition unsure, but they’re still conscious and standing.\""
    Radio "\"Are there any special notes we should be aware of?\""
    Hiraku "\"...No, nothing.\""
    Radio "\"Copy that. Inoue-san, keep a close eye on them. If possible, stay hidden until reinforcements arrive, but if you feel the need to intervene, we will leave that to your judgment.\""
    Hiraku "\"Roger that.\""
    Radio "\"Best of luck.\""
    
    play se1 "static"

    n_adv "I clipped the radio back to my belt and returned to my initial position."
    Takumi "\"—have to believe me! I-I don’t know what you’re talking about!\""
    n_adv "This time it was the victim’s voice. That’s right, just keep them talking."
    B_Brute "\"You still playin’ around, huh!?\""
    Takumi "\"K-arggh!\""
    n_adv "Alerted by the scream, I took another peek."
    
    scene bg a_alleyway
    show rain_particle
    with fade
    
    n_adv "...They’re still in the same position, but it’s hard to make out what was exactly happening."
    T_Brute "\"Three months ago, in—\""
    U_Man "\"Wait!\""
    n_adv "The main assailant walked closer to the victim."
    U_Man "\"This a sting operation? Are you being wiretapped?\""
    Hiraku "\"...!\""
    n_adv "I didn’t know where the unknown caller got his information from, but could it be because he was tapping the victim? I cursed under my breath. If the assailants figure it out, it could put the whole operation in jeopardy."
    n_adv "As if to prove my fears, the assailant suddenly shouted."
    U_Man "\"If anyone steps out, this man is dead! You hear me, any cops in hiding!?\""
    
    scene bg a_alleyway_corner
    show rain_particle
    with fade

    n_adv "Was I spotted!? My breath stuck in my throat, my heart hammering. I stayed stock-still, whole body tensed up."
    U_Man "\"Search his body.\""
    n_adv "I heard feet shuffling from the other side."
    n_adv "..."
    T_Brute "\"There’s a wallet and a phone, but nothing else.\""
    n_adv "A sigh escaped from my lips, my muscles relaxing. The worst didn’t come to pass. I stayed put, doubly careful not to make unnecessary movements."
    U_Man "\"Let’s take him to a safehouse.\""
    Hiraku "!!!"
    n_adv "My body tensed up again."
    U_Man "\"You guys wait here, I’ll take my stuff first.\""
    B_Brute "\"Alright.\""
    U_Man "\"If you try to escape... You’ll regret it, got it?\""
    Takumi "\"...Yes\""
    
    stop music fadeout 2.0
    scene bg a_alleyway
    show rain_particle
    with fade
    
    n_adv "As the sound of footsteps began to fade, I took another peek. The main assailant was walking away, and everyone’s backs were turned on me. Was this…an opportunity?"
    
    play music audio.tactics fadein 2.0

    n_adv "For an instant, time slowed down to a crawl. So much so that I could see individual raindrops falling to the ground."
    n_adv "If they’re taking the victim away…that’s bad news. Once that happens, it’ll be much more difficult to rescue him."
    n_adv "The proper procedure was to wait for reinforcements, but was there enough time for that? …Should I strike now?"
    Hiraku "\"...\""
    n_adv "Look, their backs are turned! They’re practically begging to be ambushed. It might get a little tough if they also have weapons, but…"
    n_adv "That kind of fight was just right up my alley, wasn't it?"
    Hiraku "\"{i}Inhale...{/i}\""
    n_adv "Just focus on one thing. You came here to save the victim. Do what you need to achieve that."
    Hiraku "\"{i}Exhale...{/i}\""
    n_adv "By the time the next raindrop touched the ground, I'd made my decision. The world around me started moving again."
    
    stop ambient fadeout 2.0
    stop music fadeout 2.0
    scene black 
    with fade
    pause 2.0

label ch11:
    python:
        set_info_scene("11")
        set_info_location("15")
        set_info_date(11, "Sep", "fri")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg a_alleyway
    show rain_particle
    with fade
    play ambient "rain" fadein 2.0
    
    $ show_date()

    n_adv "The unknown man had walked some distance away. Was this my chance to escape?"
    n_adv "..."
    n_adv "No, I couldn’t even escape the grip of one of these brutes, let alone both. I need something else! Think, Takumi, think! This was probably the only chance I would ever get."
    n_adv "Bribe? ...No, they were out for my blood, and I didn’t have the money for that in the first place."
    n_adv "Try to join them? …No, they already hate my guts."
    n_adv "Fuck, was there anything else I could do!?"
    n_adv "No matter how hard I racked my brain, I couldn’t figure a way out of this predicament. I cursed my own weaknesses. If only I was a little stronger, smarter, or quicker..."
    n_adv "I watched the unknown man’s back as he approached the ATM machine. With each step he took, my death sentence loomed nearer and nearer."
    n_adv "But suddenly—"
    stop ambient fadeout 2.0
    play music audio.utopia fadein 2.0
    
    T_Brute "\"Wh—\""
    Takumi "\"...?\""
    n_adv "A flash of shadow moved at lightning speed from behind the tall brute. It twisted its body, and in one graceful motion, landed a perfect roundhouse kick on his head. He immediately collapsed."
    B_Brute "\"You..!\""
    n_adv "Without wasting another second, the silhouette switched their aim to the bald brute holding me hostage. They thrust their arms forwards, and in their clasped wrists I spotted a flicker of electricity."
    Takumi "\"...!\""
    n_adv "A taser gun! Also realizing this, the brute held me even tighter, guarding himself against the taser’s trajectory."
    n_adv "For a moment, the silhouette and the brute glared at each other, neither willing to make the first move. It was only then that I got a good look at the figure. It was a woman in a dark blue garb."
    n_adv "This was it! This was my chance at escaping. Whoever you are, I will put my faith in you. Now or never!"
    n_adv "I bent my torso forwards, and mustering what strength I had left, jerked it back upwards to headbutt him straight on the nose."
    B_Brute "\"Gh!\""
    n_adv "It didn’t hit particularly hard, but his grip weakened for a split second. I struggled with everything I had and slipped out under his arms."
    n_adv "Next thing I knew, the air crackled with electricity as the prongs launched from the taser and instantly closed the gap between them. It landed squarely on the brute’s arm."
    B_Brute "\"Aghhgkkk!\""
    n_adv "His body convulsed for a second before crumpling."
    n_adv "My heart was pounding."
    Hiraku "\"I’m with the police! Follow me, I’m gonna get you out of here!\""
    n_adv "The woman quickly explained as she detached the used cartridge from the taser."
    Takumi "\"R-right!\""
    n_adv "She glanced in the direction of the unknown man. I followed her gaze. He was running back at full speed, having noticed the situation."
    n_adv "The officer immediately pulled my arm as she began to run."
    Takumi "\"!?\""
    n_adv "My left foot tripped! I doubled over, weighing the officer down with me. I glanced behind. The tall brute who fell earlier was still conscious and had his arm outstretched, gripping my foot."
    Takumi "\"Fuck!\""
    n_adv "I kicked as hard as I could, but he had my foot in a vice grip."
    T_Brute "\"Eughkhkk!?\""
    n_adv "The air crackled once again as the taser prongs landed onto the brute’s torso. His body convulsed on the ground and I was finally released."
    n_adv "However, that was enough to buy time for the unknown man to arrive."
    
    stop music fadeout 2.0

    Takumi "...!" (multiple=2)
    Hiraku "...!" (multiple=2)

    play music audio.passion fadein 2.0
    
    U_Man "\"Heaaaarghhh!\""
    n_adv "Like a bullet, he charged straight towards the police officer."
    Hiraku "\"Tsk!\""
    n_adv "She tossed the taser gun to dodge the incoming attack."
    n_adv "A flurry of punches ensued. Front jab, another jab, uppercut. She deflected all of them with precision and countered with her own jab, landing squarely on his chest."
    U_Man "\"Hk!\""
    n_adv "The guy leapt backwards to get some distance. The officer took this opportunity to move in front of me, barricading his path. I took several steps back."
    Takumi "\"...!\""
    n_adv "My palms touched the rough surface of concrete. We were pinned against the wall. Like it or not, we had to get past him to escape."
    U_Man "\"Kheh, not bad.\""
    Hiraku "\"...\""
    n_adv "He slowly circled around, scoping out his opponent. The officer remained still and steadfast."
    U_Man "\"Normally, I woulda just bailed. But officer, you know what that guy did?\""
    Hiraku "\"...\""
    U_Man "\"What he did ain’t something that could be—\""
    n_adv "He launched a surprise attack. A front jab aimed straight at the officer’s head."
    Hiraku "\"!\""
    n_adv "She expertly dodged it and countered with a side hook, but the man ducked and leapt back once more, unharmed."
    U_Man "\"—forgiven! Do us a favor and turn a blind eye to our business, will you? Just this once?\""
    Hiraku "\"I don’t know what’s between you two, but all I saw was three people ganging up on one. Whatever it was, you should settle it in court.\""
    U_Man "\"Khahaha, he’s a murderer, you know? He might backstab you from behind.\""
    n_adv "\"The officer threw a quick side glance at me.\""
    Takumi "\"No! He’s lying!\""
    n_adv "\"In that instant, he closed the gap once more. But this time, I spotted a glint of steel in his right hand. It was the knife from before!\""
    Hiraku "\"...!?\""
    n_adv "Time halted to a near standstill. The knife drew a thin arc straight to the officer’s stomach, slicing through trailing droplets of water. A hint of madness underneath his wicked grin as he lunged forwards."
    n_adv "The officer began to twist her body in an attempt to dodge, but was her reaction too late? As the blade sailed through the air, dread filled my vision. It didn’t look like she'd make it in time."
    n_adv "Please, if there’s a god out there, let her make it in time!"
    n_adv "However... when I glanced at her face, there was a glimmer of confidence in her eyes."
    Takumi "\"...?\"" 
    Takumi "\"...Ah!\""
    n_adv "That’s when I finally noticed. Her fist was raised high, ready to pounce. Her feet weren’t standing still either, they were moving to sidestep. She was ready for the surprise attack! The glance earlier must’ve been a feint!"
    n_adv "Gradually, the scene unraveled. The knife continued on its trajectory. It approached closer and closer…"
    n_adv "But it only grazed her vest!"
    n_adv "She managed to slip away in the nick of time. The grin on the unknown man gradually morphed to one of stupefaction."
    n_adv "Meanwhile, the officer’s fist was right above the man’s head, swinging down forcefully. It couldn’t miss at that range! This was the end!"
    Hiraku "Good night."
    
    play se1 "thud"

    n_adv "{i}Thud.{/i}"

    stop music fadeout 2.0
    stop ambient fadeout 2.0
    scene black
    with fade 
    pause 2.0
  

label ch12:
    python:
        set_info_scene("12")
        set_info_location("04")
        set_info_date(11, "Sep", "fri")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg car_night_rain
    with fade
    play ambient "rain_inside_car" fadein 2.0 volume 0.25
    play music audio.quiet fadein 1.0

    $ show_date()

    n_adv "The constant pulse of red lights filled my peripherals. I sat cross-legged inside one of the police cars, wrapped under a thick layer of blanket. While it did little to ease my worries, it did help stave off the piercing cold."
    n_adv "I peered through the misty windows. Several uniformed officers were huddled together under a canopy of umbrellas, probably discussing the incident. Within that group, I spotted the brown-haired officer who saved me earlier."
    n_adv "After that decisive blow, the unknown man was knocked out cold. Immediately after, my knees collapsed from exhaustion. I couldn’t remember how long I knelt on the ground."
    n_adv "Eventually, the paramedics arrived to perform a checkup on me and ask some questions. For the most part, the conversation went past as a blur. Next thing I knew, I was handed a blanket and escorted here where I’ve remained since."
    n_adv "..."
    n_adv "I recalled the attacker’s words."
    n_adv "\"Ito Genji\"... Someone with my family surname, and looked identical enough to be mistaken for me. There’s no mistaking it…right? Had I, at last, remembered…my twin brother’s name?"
    n_adv "..."
    n_adv "Looks like the officers finished their discussion. They dispersed and entered their individual cars. The brown-haired officer approached this car."
    
    stop ambient fadeout 1.0
    play se1 "car_door"
    play ambient "rain" fadein 1.0

    n_adv "Cold air seeped in as she pried the door open, her clothes dripping wet. She draped a towel over the driver’s seat before climbing on. Her face wore a solemn expression."
    
    stop ambient fadeout 1.0
    play ambient "rain_inside_car" fadein 2.0 volume 0.25
    play se1 "car_door"

    Takumi "\"Thank you for saving me earlier, officer...\""
    Hiraku "\"Inoue. And, you’re welcome.\""
    Takumi "\"Really, thank you so much. If you weren’t there, I…don’t even want to imagine what they would’ve done to me.\""
    Hiraku "\"...I’m just doing my job as a police officer.\""
    n_adv "So she said, but her face softened a little."
    Hiraku "\"Anyway, Ito-san, how are you feeling right now?\""
    Takumi "\"Nothing too bad, thanks to you. It’s just a little cold.\""
    Hiraku "\"I see, that’s good.\""
    n_adv "One by one, the red flashes around us began to fade away. The other vehicles had departed from the scene, leaving ours as the last remaining one. She turned on the car’s ignition."
    Hiraku "\"We’ll leave the questioning for tomorrow, I’ll drive you home for now. Where do you live?\""
    n_adv "I gave her the directions to my apartment."
    Hiraku "\"Oh, that’s unexpectedly close. You live around here, huh?\""
    Takumi "\"Yeah.\""
    
    play se1 "car_rev"

    n_adv "She stepped on the pedal and the car began to move."
    n_adv "I took one last look at the alleyway where it all happened. It still hadn’t fully sunk in yet. Under the light of the crescent moon, it looked just like any other alleyway around here. No trace of the earlier incident."
    n_adv "I touched the bandage on my cheek. It was the only injury I sustained. Without it…I might’ve been able to convince myself that it was all just a nightmare."
    n_adv "Those three earlier... I wonder who they were."
    Takumi "\"Inoue-san, about those three...\""
    Hiraku "\"Hm?\""
    Hiraku "\"They’re under arrest and being taken to jail right now.\""
    n_adv "She paused and drew a sharp breath."
    Hiraku "\"Actually, something’s been bugging me. They seemed to hold a grudge on you. Are you related to them in any way?\""
    Takumi "\"I’m…still not sure, honestly. I need some time to process my thoughts.\""
    Hiraku "\"Hmm… Well, take your time. Think things through tonight. I’m going to ask you again tomorrow.\""
    Takumi "\"Haha, will do.\""
    n_adv "I chuckled weakly as the conversation trailed away. My mind began to wander."
    n_adv "My long lost brother... Genji. So you are alive. Where have you been, and what are you doing right now? What did those men want with you? These questions and worries festered in my mind, yet only the whistle of the wind and clatter of rain answered me."
    
    stop ambient fadeout 1.0
    scene black
    with fade
    pause 1.0
    play ambient "rain_inside_car" fadein 1.0 volume 0.25

    scene bg car_night_rain
    with fade 

    n_adv "Before long, we arrived at my apartment."
    Hiraku "\"Here, your belongings.\""
    n_adv "She handed me a ziplock bag. Inside were my phone and wallet."
    Takumi "\"Is it ok for me to take them?\""
    Hiraku "\"Yeah. I don’t think we’ll need them as evidence. Not yet, anyway.\""
    n_adv "I checked to see if my phone was still working. It turned on normally."
    Hiraku "\"Ah, right. One more thing, add my work number to your contacts.\""
    n_adv "We exchanged phone numbers."
    Hiraku "\"Call it if you need anything.\""
    
    stop ambient fadeout 2.0
    play se1 "car_door"

    scene bg takumi_house
    show rain_particle
    with fade
    pause 1.0
    
    play se1 "car_door"
    play ambient "rain" fadein 2.0

    python:
        set_info_location("09")

    Hiraku "\"Keep the blanket if you want. Or return it tomorrow, either way is fine by me. See you tomorrow.\""
    Takumi "\"Thank you again, Inoue-san.\""
    n_adv "\"We bid our farewells. As the car lights slowly faded away, I turned around to face the front steps. Rainwater trickled down from the roof, forming puddles at the foot of the railing. After all’s said and done, I was back at this old apartment once again.\""
    n_adv "No... Something was different this time. After years of evading me, I finally, finally regained my brother’s name."
    Takumi "\"Genji...\""
    n_adv "It had a nice ring to it."
    Takumi "\"Ito Genji.\""
    n_adv "Savoring how the name rolled off the tongue, I burned it into my memory. A soft, hopeful smile formed on my lips."
    n_adv "While a mountain of questions lingered in my mind, I was glad to at least have the first and most important piece of the puzzle."
    
    stop ambient fadeout 2.0

    n_adv "Was this the wind of change I sought? Who knows, but it’s better than nothing."

    play se1 "door_open"

    n_adv "{i}Click.{/i}"

    scene bg takumi_inside
    with fade

    python:
        set_info_location("10")
        

    n_adv "Unlocking the door, a bright-lit corridor greeted me. Even this normally depressing space radiated a trace of warmth now. Almost like…"
    Takumi "\"I’m home.\""
    n_adv "Only the silence replied. Perhaps one day, if Genji ever returns..."
    Takumi "\"{i}Yaaaawn.{/i}\""
    n_adv "As if on cue, the moment I stepped inside, my eyelids grew weary. I’ll head to bed early tonight. I had a feeling that tomorrow…there will be yet more winds of change to come."
    
    play se1 "door_open"
    stop ambient fadeout 2.0
    stop music fadeout 2.0
    scene black
    with fade 

    n_adv "{i}Click.{/i}"

    pause 2.0

label ch13:
    python:
        set_info_scene("13")
        set_info_location("13")
        set_info_date(11, "Sep", "fri")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg bar_inside_lounge
    with fade
    play music audio.meeting fadein 2.0

    $ show_date()

    n_adv "Seated inside one of the sofas, the bartender brought the glass to his lips. Inside it was a sliver of pale white liquid. He had poured himself just a sip of his favorite white wine in celebration."
    TBD "\"It worked out well, didn’t it?\""
    n_adv "He whispered, seemingly to no one."
    n_adv "In response, however, the air stirred, gradually growing denser. The peculiar presence appeared once more."
    noname_adv "\"A fluke, that’s what it was.\""
    TBD "\"A success nonetheless.\""
    noname_adv "\"What would’ve happened if she refused?\""
    n_adv "He paused in thought for a moment."
    TBD "\"Then... The next approach would be due.\""
    noname_adv "\"Tsk, that again… Fine, struggle as much as you want. Just know that when you inevitably fail, I’ll be right around the corner.\""
    n_adv "The voice echoed away as the air dissipated. The room regained its tranquility as the bartender was once again left alone."
    TBD "\"...\""
    n_adv "He brought the tip of the glass to his lips and tilted it, but only a single drop of wine remained, sliding down the surface. Perhaps he ought to pour a little more, he caught himself thinking."
    TBD "\"...No, there’s still more to do.\""
    n_adv "With a light groan, he pushed himself off the sofa. The ordeal was far from over."
    
    stop music fadeout 2.0
    scene black 
    with fade
    pause 2.0

label ch14:
    python:
        set_info_scene("04")
        set_info_location("16")
        set_info_date(12, "Sep", "sat")
        set_info_time("night")

    scene placeholder
    with fade
    pause 2.0

    scene bg orientall_hall
    with fade
    play music audio.flame fadein 2.0

    $ show_date()

    n_adv "Inside a majestic oriental hall decorated with golden ornaments and the finest quality of wooden sculptures, an assembly of solemn figures had been gathered."
    n_adv "These people each commanded their own dignity and authority, yet their expressions remained respectful. Their reverent gazes were directed at the throne at the center of the chamber."
    Empress "\"Is that true, Lieutenant Odawara?\""
    n_adv "From atop the throne, the empress’s voice resounded throughout the hall. Even though she was young, her voice possessed such dignity befitting of the room that none dared to question her."
    n_adv "Upon being addressed, the subordinate who had been kneeling before her finally raised his head."
    Empress "\"Yes, your excellency. At around eight thirty p.m. earlier today, they were arrested by the police.\""
    Voice "\"Do you have anything to say on the matter?\""
    Odawara "\"I..have nothing to offer but my deepest apology for their mistakes, your excellency.\""
    n_adv "The subordinate lowered his head once more, bowing deeply."
    Voice "\"Very well, apology accepted. You are dismissed.\""
    n_adv "She waved her hand in dismissal. However, the lieutenant made no motions to stand up."
    Odawara "\"Your excellency, if I may be allowed to ask…\""
    Advisor "\"Lieutenant, are you defying—\""
    n_adv "A middle-aged man began to admonish the lieutenant, but the empress raised a hand to halt his words. He reluctantly backed off from his fervor."
    Empress "\"Continue.\""
    Odawara "\"Thank you very much, your excellency. If I may ask, what will happen to my men?\""
    Empress "\"...Do not worry. They will be given the usual treatment.\""
    Odawara "\"Thank you very much, your excellency.\""
    Empress "You are dismissed."
    n_adv "This time, her tone left no room for negotiations The lieutenant swiftly stood up, bowed deeply, and left the room. The giant double doors creaked softly as they slid shut."
    n_adv "Silence returned to the hall. Only the empress and her closest confidants remained."
    n_adv "..."
    Empress "\"Your men have been observing them, correct? What of the experiment?\""
    n_adv "With her chin, she gestured towards one of the several advisors lined by her side. The one she picked, an elderly man in white robes, replied gravely."
    E_Advisor "\"A complete failure, unfortunately...\""
    Empress "\"So we need the key after all.\""
    E_Advisor "\"Yes…\""
    n_adv "The empress contemplated for a moment before rising from her throne. The hems of her kimono brushed against the tatami mats as she strode across the hall. Her steps soundless, her every movement performed with grace befitting of a ruler. "
    n_adv "The advisors’ eyes followed her as she approached the large window at the end of the chamber."
    
    scene bg moon
    with fade
    pause 1.0
    play ambient "longrain" fadein 1.0

    n_adv "Her gaze peered through the veil of rain, to the crescent moon that lay beyond. She then turned around to face her confidants once more."
    n_adv "Their expressions tensed in anticipation. The empress’s eyes burned with sharp determination, and they recognized it."
    
    scene bg orientall_hall
    with fade

    Empress "\"Prepare our men. Begin the operation tomorrow.\""
    Advisor "\"But your excellency... Isn’t it a little early?\""
    Empress "\"The longer we wait, the larger his advantage grows. We mustn’t permit that.\""
    Advisors "\"...\""
    
    scene bg moon
    with fade

    n_adv "She returned her gaze to the moon."
    n_adv "Soon, when it shines the brightest, it would be a fitting time to declare their successorship. But now, when it was nearing its darkest, it was the perfect time to strike under the shadows."
    Empress "\"Soon, we will regain our former glory. So long as you follow me, our rise will be as certain as the moon in the night sky. Never forget that.\""
    n_adv "She had the determination and ability to turn their goals into reality, and her followers recognized that. By the oath of the coiling dragon around their arms, they would sooner lay their own life than let their empress into harm’s way."
    Advisors "\"Understood, your excellency.\""
    n_adv "The advisors bowed in unison."
    n_adv "And so, the shadow of the moon began its descent on the city."
    
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene black
    with fade
    pause 2.0
