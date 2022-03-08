
define bgm_titles = {
    "bgm_00" : _("The Door"),
    "bgm_01" : _("Rainfall"), 
    "bgm_02" : _("The Window Overlooking All Things"),
    "bgm_03" : _("Kamikaze"),
    "bgm_04" : _("Tokyo at the Night"),
    "bgm_05" : _("Blue Garnet"),
    "bgm_06" : _("Dead End Strike"),
    "bgm_07" : _("Osmanthus"),
    "bgm_08" : _("The Night Before"),
    "bgm_09" : _("Feelings of a Distant Day"),
    "bgm_10" : _("Meeting extension"),
    "bgm_11" : _("Cold Fish"),
    "bgm_12" : _("Fear"),
    "bgm_13" : _("Tactics"),
    "bgm_14" : _("In Pursuit of Utopia"),
    "bgm_15" : _("Passion of Sorrow"),
    "bgm_16" : _("Quiet Rain"),
    "bgm_17" : _("Flame Podium"),
    "bgm_18" : _("Suspicious (Temp)"),
    "bgm_19" : _("Answer (Temp)"),
    "bgm_20" : _(""),
}

define scenes = {
    "01" : _("???"),
    "02" : _("Work Day"),
    "03" : _("The Falldown"),
    "04" : _("CH4"),
    "05" : _("CH5"),
    "06" : _("CH6"),
    "07" : _("CH7"),
    "08" : _("CH8"),
    "09" : _("CH9"),
    "10" : _("CH10"),
    "11" : _("CH11"),
    "12" : _("CH12"),
    "13" : _("CH13"),
    "14" : _("CH14"),
    "15" : _("CH15"),
}

define locations = {
    "01" : {"name" : _("？？？"), "tip" : ""},
    "02" : {"name" : _("Yasuda Office"), "tip" : "The office where white collar workers are paid to work until death. It is also Where Takumi works at, and Masashi's company"},
    "03" : {"name" : _("Yodoyabashi Street"), "tip" : "The usual road for workers to go through, a lot of things happen here during the day, noon and night... which is everyday."},
    "04" : {"name" : _("Hiraku's Car"), "tip" : "Hiraku's Vehicle, she uses it for chasing the bad guys and serving justice while at it."},
    "05" : {"name" : _("Some road in Tokyo"), "tip" : "Road that is taken by any other person, be it a human or an animal."},
    "06" : {"name" : _("Nagara Bridge"), "tip" : "The bridge that connects this and that."},
    "07" : {"name" : _("Train"), "tip" : "The bridge that connects this and that."},
    "08" : {"name" : _("Train station"), "tip" : "The bridge that connects this and that."},
    "09" : {"name" : _("Exit place after train"), "tip" : "The bridge that connects this and that."},
    "10" : {"name" : _("Takumi's House"), "tip" : "The bridge that connects this and that."},
    "11" : {"name" : _("Airin Street"), "tip" : "The bridge that connects this and that."},
    "12" : {"name" : _("Abandoned Alleyway"), "tip" : "The bridge that connects this and that."},
    "13" : {"name" : _("Z-Bar"), "tip" : "The bridge that connects this and that."},
    "14" : {"name" : _("Police Office"), "tip" : "The bridge that connects this and that."},
    "15" : {"name" : _("Abandoned Alleyway (2)"), "tip" : "The bridge that connects this and that."},
    "16" : {"name" : _("Oriental Hall"), "tip" : "The bridge that connects this and that."},
}


init:

    # initialize people's page
    $ notebook_people = None

    ### people's page ###################
    $ notebook_page_people = 1
    $ person_of_interest = 0
    $ available_page_people = 1
    $ persistent.person_of_interests = 0  
    
    # list of persons also the buttons for them
    define person1 = False
    define person2 = False
    define person3 = False
    define person4 = False
    define person5 = False
    define person6 = False
    define person7 = False
    define person8 = False
    define person9 = False
    define person10 = False
    define person11 = False
    define person12 = False
    define person13 = False
    define person14 = False
    define person15 = False
    define person16 = False
    define person17 = False
    define person18 = False
    define person19 = False
    define person20 = False



    # person1 note on the portrait
    define person_info1 = None

    # person1 note below the portrait
    define person_note1 = None
    define person_note1_1 = None
    define person_note1_2 = None
    define person_note1_3 = None
    define person_note1_4 = None
    define person_note1_5 = None
    define person_note1_6 = None 
    define person_note1_7 = None
    define person_note1_8 = None
    define person_note1_9 = None
    define person_note1_10 = None



    # person2 note on the portrait
    define person_info2 = None

    # person2 note below the portrait
    define person_note2 = None
    define person_note2_1 = None
    define person_note2_2 = None
    define person_note2_3 = None
    define person_note2_4 = None
    define person_note2_5 = None
    define person_note2_6 = None
    define person_note2_7 = None
    define person_note2_8 = None
    define person_note2_9 = None
    define person_note2_10 = None



    # person2 note on the portrait
    define person_info3 = None

    # person2 note below the portrait
    define person_note3 = None
    define person_note3_1 = None
    define person_note3_2 = None
    define person_note3_3 = None
    define person_note3_4 = None
    define person_note3_5 = None
    define person_note3_6 = None
    define person_note3_7 = None
    define person_note3_8 = None
    define person_note3_9 = None
    define person_note3_10 = None



    # person2 note on the portrait
    define person_info4 = None

    # person2 note below the portrait
    define person_note4 = None
    define person_note4_1 = None
    define person_note4_2 = None
    define person_note4_3 = None
    define person_note4_4 = None
    define person_note4_5 = None
    define person_note4_6 = None
    define person_note4_7 = None
    define person_note4_8 = None
    define person_note4_9 = None
    define person_note4_10 = None



    # person2 note on the portrait
    define person_info5 = None

    # person2 note below the portrait
    define person_note5 = None
    define person_note5_1 = None
    define person_note5_2 = None
    define person_note5_3 = None
    define person_note5_4 = None
    define person_note5_5 = None
    define person_note5_6 = None
    define person_note5_7 = None
    define person_note5_8 = None
    define person_note5_9 = None
    define person_note5_10 = None



    # person2 note on the portrait
    define person_info6 = None

    # person2 note below the portrait
    define person_note6 = None
    define person_note6_1 = None
    define person_note6_2 = None
    define person_note6_3 = None
    define person_note6_4 = None
    define person_note6_5 = None
    define person_note6_6 = None
    define person_note6_7 = None
    define person_note6_8 = None
    define person_note6_9 = None
    define person_note6_10 = None



    # person2 note on the portrait
    define person_info7 = None

    # person2 note below the portrait
    define person_note7 = None
    define person_note7_1 = None
    define person_note7_2 = None
    define person_note7_3 = None
    define person_note7_4 = None
    define person_note7_5 = None
    define person_note7_6 = None
    define person_note7_7 = None
    define person_note7_8 = None
    define person_note7_9 = None
    define person_note7_10 = None



    # person2 note on the portrait
    define person_info8 = None

    # person2 note below the portrait
    define person_note8 = None
    define person_note8_1 = None
    define person_note8_2 = None
    define person_note8_3 = None
    define person_note8_4 = None
    define person_note8_5 = None
    define person_note8_6 = None
    define person_note8_7 = None
    define person_note8_8 = None
    define person_note8_9 = None
    define person_note8_10 = None



    # person2 note on the portrait
    define person_info9 = None

    # person2 note below the portrait
    define person_note9 = None
    define person_note9_1 = None
    define person_note9_2 = None
    define person_note9_3 = None
    define person_note9_4 = None
    define person_note9_5 = None
    define person_note9_6 = None
    define person_note9_7 = None
    define person_note9_8 = None
    define person_note9_9 = None
    define person_note9_10 = None



    # person2 note on the portrait
    define person_info10 = None

    # person2 note below the portrait
    define person_note10 = None
    define person_note10_1 = None
    define person_note10_2 = None
    define person_note10_3 = None
    define person_note10_4 = None
    define person_note10_5 = None
    define person_note10_6 = None
    define person_note10_7 = None
    define person_note10_8 = None
    define person_note10_9 = None
    define person_note10_10 = None

    
init:

    ### case's page ####################
    $ notebook_case = None
    $ notebook_page_case = 1
    $ case_of_interest = 0
    $ available_page_case = 1
    $ persistent.case_of_interests = 0

    # list of persons also the buttons for them
    define case1 = False
    define case2 = False
    define case3 = False
    define case4 = False
    define case5 = False
    define case6 = False
    define case7 = False
    define case8 = False
    define case9 = False
    define case10 = False

    # info besides the image case
    define case_note1 = None
    define case_note1_1 = None
    define case_note1_2 = None
    define case_note1_3 = None
    define case_note1_4 = None
    define case_note1_5 = None
    define case_note1_6 = None
    define case_note1_7 = None
    define case_note1_8 = None
    define case_note1_9 = None
    define case_note1_10 = None

    define case_note2 = None
    define case_note2_1 = None
    define case_note2_2 = None
    define case_note2_3 = None
    define case_note2_4 = None
    define case_note2_5 = None
    define case_note2_6 = None
    define case_note2_7 = None
    define case_note2_8 = None
    define case_note2_9 = None
    define case_note2_10 = None

init: 
    $ notebook_tip = None
    $ notebook_page_tip = 1
    $ tip_of_interest = 0
    $ available_page_tip = 1
    $ persistent.tip_of_interests = 0

    # List of words
    define tip1 = False
    define tip2 = False
    define tip3 = False
    define tip4 = False
    define tip5 = False
    define tip6 = False
    define tip7 = False
    define tip8 = False
    define tip9 = False
    define tip10 = False

init -5:

    define times = {
        None : { "label" : "", "icon" : None},
        "morning" : { "label" : _("朝"), "icon" : "gui/game_menu_icons/sunrise.png" },
        "day" : { "label" : _("昼"), "icon" : "gui/game_menu_icons/midday.png" },
        "evening" : { "label" : _("夕方"), "icon" : "gui/game_menu_icons/sunset.png" },
        "night" : { "label" : _("夜"), "icon" : "gui/game_menu_icons/midnight.png" },
    }

