## Game Menu screen ############################################################


screen game_menu():
    key "mousedown_3" action Return()
    
    style_prefix "game_menu" tag case
    
    $ hours_played = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutes_played = convertSeconds( renpy.get_game_runtime() )[1]
    $ seconds_played = convertSeconds( renpy.get_game_runtime() )[2]
    $ bgm_title = get_current_bgm_title()


    add "gui/game_frames/right_click_bg.png"
               
    ### The state of the notebook itself #########################################

    if notebook_info == None:
        add "gui/game_frames/closed_notebook.png" xalign 0.35 yalign 0.5
    else:
        frame:
            background None
            add "gui/game_frames/black_image.png" xoffset 120 yoffset 160

            hbox:
                imagebutton:
                    xoffset 530
                    yoffset 102.5
                    idle "gui/gui_buttons/GUI notebook_buttons/tips_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/tips_selected.png"
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    action ShowMenu("tips_page", transition= None)
                imagebutton:
                    xoffset 200
                    yoffset 102.5
                    idle "gui/gui_buttons/GUI notebook_buttons/cases_idle.png"
                    hover "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                    selected_idle "gui/gui_buttons/GUI notebook_buttons/cases_selected.png"
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    action ShowMenu("gallery", transition= None)

    ### The state of the notebook page for people's page ##########################

            frame:
                background None
                xoffset 70
                yoffset 50
                if person_of_interest == 0:
                    add "gui/game_frames/notebook_paper_cases.png" xoffset 60 yoffset 100.5
                else:
                    add "gui/game_frames/notebook_paper_people.png" xoffset 60 yoffset 100.5
                hbox:
                    imagebutton:
                        xoffset 127.5
                        yoffset 42.5
                        idle "gui/gui_buttons/GUI notebook_buttons/people_idle.png"
                        hover "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                        selected_idle "gui/gui_buttons/GUI notebook_buttons/people_selected.png"
                        hover_sound None
                        activate_sound "audio/sfx/pageflip.wav"
                        action ShowMenu("game_menu", transition= None)

    ### The number of people and their profile sprites ############################################

    if person_of_interest == 1:
        add "gui/people_info/profile1.png" xpos 729 ypos 242        
    elif person_of_interest == 2:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 3:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 4:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 5:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 6:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 7:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 8:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 9:
        add "gui/people_info/profile1.png" xpos 729 ypos 242
    elif person_of_interest == 10:
        add "gui/people_info/profile1.png" xpos 729 ypos 242    


    ### The number of buttons on the list of people ########################################

    if notebook_page_people == 1:
        vbox:
            xpos 200 
            ypos 242
            if person1 == True:
                textbutton "Takumi":
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    text_size 36
                    if person_of_interest == 1:
                        action SetVariable("person_of_interest", 1)
                    else:
                        action SetVariable("person_of_interest", 1)
            if person2 == True:
                textbutton "Hiraku":
                    yoffset -10
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 2:
                        action SetVariable("person_of_interest", 2) 
                    else:
                        action SetVariable("person_of_interest", 2)  
            if person3 == True:
                textbutton "Hiraku":
                    yoffset -15
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 3:
                        action SetVariable("person_of_interest", 3) 
                    else:
                        action SetVariable("person_of_interest", 3) 
            if person4 == True:
                textbutton "TBD":
                    yoffset -20
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 4:
                        action SetVariable("person_of_interest", 4) 
                    else:
                        action SetVariable("person_of_interest", 4)
            if person5 == True:
                textbutton "Hikari":
                    yoffset -25
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 5:
                        action SetVariable("person_of_interest", 5) 
                    else:
                        action SetVariable("person_of_interest", 5)  
            if person6 == True:
                textbutton "Maeda":
                    yoffset -30
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 6:
                        action SetVariable("person_of_interest", 6) 
                    else:
                        action SetVariable("person_of_interest", 6)
            if person7 == True:
                textbutton "Tetsuro":
                    yoffset -35
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 7:
                        action SetVariable("person_of_interest", 7) 
                    else:
                        action SetVariable("person_of_interest", 7)
            if person8 == True:
                textbutton "Kotani":
                    yoffset -40
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 8:
                        action SetVariable("person_of_interest", 8) 
                    else:
                        action SetVariable("person_of_interest", 8)
            if person9 == True:
                textbutton "Eizo":
                    yoffset -45
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 9:
                        action SetVariable("person_of_interest", 9) 
                    else:
                        action SetVariable("person_of_interest", 9)
            if person10 == True:
                textbutton "Genji":
                    yoffset -50
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 10:
                        action SetVariable("person_of_interest", 10) 
                    else:
                        action SetVariable("person_of_interest", 10)
    elif notebook_page_people == 2:
        vbox:
            xpos 200 
            ypos 242
            if person11 == True:
                textbutton "Takumi":
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    text_size 36
                    if person_of_interest == 11:
                        action SetVariable("person_of_interest", 11)
                    else:
                        action SetVariable("person_of_interest", 11)
            if person12 == True:
                textbutton "Nakamura":
                    yoffset -10
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 12:
                        action SetVariable("person_of_interest", 12) 
                    else:
                        action SetVariable("person_of_interest", 12)  
            if person13 == True:
                textbutton "Hiraku":
                    yoffset -15
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 13:
                        action SetVariable("person_of_interest", 13) 
                    else:
                        action SetVariable("person_of_interest", 13) 
            if person14 == True:
                textbutton "TBD":
                    yoffset -20
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 4:
                        action SetVariable("person_of_interest", 4) 
                    else:
                        action SetVariable("person_of_interest", 4)
            if person15 == True:
                textbutton "Hikari":
                    yoffset -25
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 15:
                        action SetVariable("person_of_interest", 15) 
                    else:
                        action SetVariable("person_of_interest", 15)  
            if person16 == True:
                textbutton "Maeda":
                    yoffset -30
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 16:
                        action SetVariable("person_of_interest", 16) 
                    else:
                        action SetVariable("person_of_interest", 16)
            if person17 == True:
                textbutton "Tetsuro":
                    yoffset -35
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 17:
                        action SetVariable("person_of_interest", 17) 
                    else:
                        action SetVariable("person_of_interest", 17)
            if person18 == True:
                textbutton "Kotani":
                    yoffset -40
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 18:
                        action SetVariable("person_of_interest", 18) 
                    else:
                        action SetVariable("person_of_interest", 18)
            if person19 == True:
                textbutton "Eizo":
                    yoffset -45
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 19:
                        action SetVariable("person_of_interest", 19) 
                    else:
                        action SetVariable("person_of_interest", 19)
            if person20 == True:
                textbutton "Genji":
                    yoffset -50
                    hover_sound None
                    activate_sound "audio/sfx/pageflip.wav"
                    text_font "fonts/Kalam-Regular.ttf"
                    if person_of_interest == 20:
                        action SetVariable("person_of_interest", 20) 
                    else:
                        action SetVariable("person_of_interest", 20)
    
    ### The pages flips ###############

    if available_page_people >= 2:
        imagebutton:
            # NEXT   
            idle "gui/cases_ui/right.png"
            hover "gui/cases_ui/right_hover.png"
            xpos 440 ypos 742
            hover_sound None
            activate_sound "audio/sfx/pageflip.wav"
            if notebook_page_people == available_page_people:
                action NullAction()
            else:
                action SetVariable("notebook_page_people", notebook_page_people + 1)
        imagebutton:
            # PREVIOUS
            idle "gui/cases_ui/left.png"
            hover "gui/cases_ui/left_hover.png"
            xpos 305 ypos 723
            hover_sound None
            activate_sound "audio/sfx/pageflip.wav"
            if notebook_page_people == 1:
                action NullAction()
            else:
                action SetVariable("notebook_page_people", notebook_page_people - 1)


    ### The content of each people's information per page ###################################

    frame:
        background None
        xpadding 10
        ypadding 10
        xpos 725
        ypos 420
        xsize 482
        ysize 500

        ### Information near the image sprite #######################

        hbox:
            xoffset 250
            yoffset -155
            if person_of_interest == 1:
                if person_note1 == True:
                    if person_info1 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Takumi" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -150
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)] xalign 0.5
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Office Worker" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)] xalign 0.5
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Takumi" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -115
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)] xalign 0.5
                        vbox:
                            yoffset 77.5 xoffset -150
                            text "{color=#000}Salaryman" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)] xalign 0.5
            if person_of_interest == 2:
                if person_note2 == True:
                    if person_info2 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}21" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}21" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 3:
                if person_note3 == True:
                    if person_info3 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 4:
                if person_note4 == True:
                    if person_info4 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 5:
                if person_note5 == True:
                    if person_info5 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 6:
                if person_note6 == True:
                    if person_info6 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 7:
                if person_note7 == True:
                    if person_info7 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 8:
                if person_note8 == True:
                    if person_info8 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 9:
                if person_note9 == True:
                    if person_info9 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
            if person_of_interest == 10:
                if person_note10 == True:
                    if person_info10 == "redacted":
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]
                    else:
                        vbox:
                            yoffset -55
                            text "{color=#000}Inoue Hiraku" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.05, "#00000099", 0, 0)]
                        vbox:
                            yoffset 10 xoffset -190
                            text "{color=#000}19" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.65, "#00000099", 0, 0)]
                        vbox:
                            yoffset 77.5 xoffset -220
                            text "{color=#000}Police" size 30 font "fonts/Kalam-Regular.ttf" outlines [(0.75, "#00000099", 0, 0)]


        ### Information content about themselves ################################

        viewport:
            scrollbars "vertical"
            xoffset 10
            yoffset -5
            mousewheel True
            draggable True
            side_yfill True

            vbox:
                if person_of_interest == 1:
                    if person_note1 == True:
                        add None
                    if person_note1_1 == "first_note":
                        null height 20
                        text "{color=#000}- Works at Yasuda Farmers Company" size 32 font "fonts/Kalam-Regular.ttf"
                    elif person_note1_1 == "first_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
                    if person_note1_2 == "second_note":
                        null height 20
                        text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"
                    elif person_note1_2 == "second_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
                if person_of_interest == 2:
                    if person_note2 == True:
                        add None
                    if person_note2_1 == "first_note":
                        null height 20
                        text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"
                    elif person_note2_1 == "first_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
                    if person_note2_2 == "second_note":
                        null height 20
                        text "{color=#000}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." size 30 font "fonts/Kalam-Regular.ttf"
                    elif person_note2_2 == "second_note_redacted":
                        null height 20
                        text "{color=#000}{s}Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/s}, my first iteration was wrong," size 30 font "fonts/Kalam-Regular.ttf"
            

### INFO PANEL ####################


    vbox style_suffix "chaptername_vbox":
        
        xalign 0.5
        xoffset 610
        yalign 0.175
        text save_name style_suffix "chaptername_text" xalign 0.5
        
        hbox:
            spacing 15
            xalign 0.5

            add get_time_icon() xsize 60 ysize 60 xoffset -5 yoffset 0

            text "[gameinfo_date]" style_suffix "date_text"

    on "show" action [Preference("auto-forward", "disable"), SetField(config, "skipping", None)]

    use info_panel(_(" BGM"), get_current_bgm_title(), "gui/game_menu_icons/audio-playlist_w.png", (0.925, 0.325))

    use info_panel(_(" Location"), get_location_name(), "gui/game_menu_icons/map_w.png", (0.925, 0.550))

    use info_panel(_(" Info"), get_location_tip(), "gui/game_menu_icons/comment-bubble_w.png", (0.925, 0.775))

    frame:
        xoffset 135
        yoffset 895
        background None
        if notebook_info == True:
            text "Playtime:" size 35 xoffset 51 yoffset 0 color "#000" font "fonts/Kalam-Regular.ttf"
            hbox:
                yoffset 0
                xoffset 200
                text "[hours_played]:[minutes_played]:[seconds_played]" color "#000" font "fonts/Kalam-Regular.ttf" size 35
        else:
            text ""    
    imagebutton:
        xalign 0.95
        yalign 0.925
        idle "gui/gui_buttons/GUI main_buttons/back1_idle.png"
        hover "gui/gui_buttons/GUI main_buttons/back1_selected.png"
        selected_idle "gui/gui_buttons/GUI main_buttons/back1_selected.png"
        insensitive None
        hover_sound None
        activate_sound "audio/sfx/clickcool.wav"
        action Return()

init -2:

    style game_menu_chaptername_vbox:
        spacing 15
        align (0.85, 0.15)

    style game_menu_chaptername_text:
        font "fonts/Poppins-Light.ttf"
        size 48
        xalign 0.5
        xoffset 0

    style game_menu_date_text:
        font "fonts/Poppins-Light.ttf"
        size 30
        line_spacing 0
        line_leading 0
        yoffset 7.5

    style game_menu_tooltip_text:
        font "fonts/Poppins-Light.ttf"
        align (0.5, 0.5)
        size 18
        color "#fff"
        outlines [(1, "#00000099", 0, 0)]
        kerning 0
        line_spacing 0
        line_leading 0
        layout "subtitle"
        text_align 0.5