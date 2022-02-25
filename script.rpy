﻿
define config.rollback_enabled = False
define _dismiss_pause = False

init:
    $ config.keymap['game_menu'].remove('mouseup_3')

init python:
    skipping = False
    preference_page = True
    current_mode = "main"
    nvl_mod = False
    notebook_info = None

init -3:

    define audio.door = "<loop 000.000 to 83.000>bgm_00"
    define audio.rainfall = "<loop 000.000 to 178.000>bgm_01"
    define audio.window = "<loop 000.000 to 312.000>bgm_02"
    define audio.kamikaze = "<loop 000.000 to 040.000>bgm_03"
    define audio.tokyo = "<loop 000.000 to 190.000>bgm_04"
    define audio.blue = "<loop 000.000 to 135.000>bgm_05"
    define audio.strike = "<loop 000.000 to 123.000>bgm_06"
    define audio.osmanthus = "<loop 000.000 to 187.000>bgm_07"
    define audio.night = "<loop 000.000 to 202.000>bgm_08"
    define audio.distant = "<loop 000.000 to 141.000>bgm_09"
    define audio.meeting = "<loop 000.000 to 136.000>bgm_10"
    define audio.cold = "<loop 000.000 to 151.000>bgm_11"
    define audio.fear = "<loop 000.000 to 150.019>bgm_12"
    define audio.strolling = "<loop 000.0167 to 150.019>bgm_13"

return

label _hide_windows_override:

    if renpy.context()._menu:
        return

    if _windows_hidden:
        return

    python:
        _windows_hidden = True

        config.skipping = None
        renpy.run(Preference("auto-forward", "disable"))
        renpy.context_dynamic("_last_voice_play")
        renpy.transition(Dissolve(0.2))

        ui.saybehavior(dismiss=['dismiss', 'hide_windows', 'game_menu', 'rollback', 'rollforward', 'toggle_skip', 'skip'])
        ui.interact(suppress_overlay=True, suppress_window=True)


        renpy.transition(Dissolve(0.2))

        _windows_hidden = False

    return

label chapter1:
    stop music fadeout 2.0
    $_dismiss_pause = False
    scene white
    hide screen navigation
    hide screen chapters
    hide screen main_menu
    $ renpy.transition(white3)
    $ renpy.pause(5, hard = True)
    $ renpy.run(Start("ch1"))

label chapter2:
    stop music fadeout 2.0
    $_dismiss_pause = False
    scene white
    hide screen navigation
    hide screen chapters
    hide screen main_menu 
    $ renpy.transition(white3)
    $ renpy.pause(5, hard = True)
    $ renpy.run(Start("prologue"))

label chapter3: 
    stop music fadeout 2.0
    $_dismiss_pause = False
    scene white
    hide screen navigation
    hide screen chapters
    hide screen main_menu 
    $ renpy.transition(white3)
    $ renpy.pause(5, hard = True)
    $ renpy.run(Start("prologue"))



init -2 python:

    if persistent.firstchapter_clear is None:
        persistent.firstchapter_clear = False

    if persistent.secondchapter_clear is None:
        persistent.secondchapter_clear = False
    
    if persistent.thirdchapter_clear is None:
        persistent.thirdchapter_clear = False

    if persistent.seen_words is None:
        persistent.seen_words = {}

    
init -2 python:
    
    import datetime

    def set_info_scene(scene_id):
        global save_name
        
        if scene_id in scenes:
            save_name = scenes[scene_id]
        else:
            raise ValueError("The scene id '{0}' is unknown.".format(scene_id))

    def set_info_time(time_id):
        global gameinfo_time
        
        if time_id in times:
            gameinfo_time = time_id
        else:
            raise ValueError("The time id '{0}' is unknown.".format(time_id))

    def set_info_date(month, day, weekday):
        global gameinfo_date
        
        if (weekday != "mon" and 
            weekday != "tue" and 
            weekday != "wed" and 
            weekday != "thu" and 
            weekday != "fri" and
            weekday != "sat" and
            weekday != "sun" and
            weekday != "???"):
            raise ValueError("No such a weekday: {0}.".format(weekday))
        
        # gameinfo_date = "{0} {1} ({2})".format(month.zfill(2), day.upper(), weekday.upper())
        gameinfo_date = "{0} {1} ({2})".format(str(month).zfill(2), str(day).zfill(2).upper(), weekday.upper())
        # gameinfo_date = "{0:02d} {1:02d} ({2:s})".format(month, day, weekday.upper())
    def get_current_bgm_title():
            
            now_playing = renpy.music.get_playing()
            
            if now_playing:
                now_playing = now_playing[-6:]
                if now_playing in bgm_titles:
                    return bgm_titles[now_playing]
            
            return 

    def set_info_location(location_id):
        global gameinfo_location
        
        if location_id in locations:
            gameinfo_location = location_id
        else:
            raise ValueError("The location id '{0}' is unknown.".format(location_id))
    
    def get_time_icon():
        if gameinfo_time in times:
            return times[gameinfo_time]["icon"]
        else:
            return None

    def get_location_name():       
        if gameinfo_location in locations:  
            return locations[gameinfo_location]["name"]
        else:
            return ""

    def get_location_tip():       
        if gameinfo_location in locations:  
            return locations[gameinfo_location]["tip"]
        else:
            return ""

    def show_date():
        global gameinfo_date

        if config.skipping:
            if renpy.get_screen("hud"):
                renpy.hide_screen("hud")
                hud = True
            else:
                return
                hud = False
        
        if not renpy.get_screen("hud") and not renpy.in_rollback():
            renpy.show_screen("hud")
    
    def show_people():

        if config.skipping:
            if renpy.get_screen("hud1"):
                renpy.hide_screen("hud1")
            else:
                return
        if not renpy.get_screen("hud1") and not renpy.in_rollback():
            renpy.show_screen("hud1")
    
    def show_cases():   

        if config.skipping:
            if renpy.get_screen("hud2"):
                renpy.hide_screen("hud2")
            else:
                return
        if not renpy.get_screen("hud2") and not renpy.in_rollback():
            renpy.show_screen("hud2")

    def show_tips():

        if config.skipping:
            if renpy.get_screen("hud3"):
                renpy.hide_screen("hud3")
            else:
                return
        if not renpy.get_screen("hud3") and not renpy.in_rollback():
            renpy.show_screen("hud3")
            
    def convertSeconds(scs):
        ##convertimos los segundos a entero
        scs = round(scs)

        ##ahora este valor pasará a ser un hh:mm:ss
        scs = str(datetime.timedelta(seconds=scs))
        ##se convierte ahora en un array
        scs = scs.split(":")

        return scs


define gameinfo_time = ""
define gameinfo_date = ""
define gameinfo_location = ""
define gameinfo_seen_chapters = ""

init -2 python:

    def get_seen_words():
        global words_seen_dictionary
        
        words_dic = {}
        words = words_seen_dictionary.split(",")[:-1]
        
        for word in words:
            split_word = word.split("-")
            
            if split_word[0] not in words_dic:
                words_dic[split_word[0]] = []
            
            words_dic[split_word[0]].append(split_word[1])
        
        return words_dic

    def add_seen_words(words_name):
        global words_seen_dictionary
        
        if words_name not in word_definition:
            raise Exception("'" + words_name + "' is not a valid name.")
        
        if words_name not in words_seen_dictionary.split(","):
            words_seen_dictionary += words_name + ","
        
        
        words_name_split = words_name.split("-")
        key = words_name_split[0]
        value = words_name_split[1]
        
        if key not in persistent.seen_words:
            persistent.seen_words[key] = []
        
        if value not in persistent.seen_words[key]:
            persistent.seen_words[key].append(value)
            
    def sort_word_buttons(key):
        
        split_key = key.split("_")
        
        split_key_len = len(split_key) 
        
        if split_key_len > 2 or split_key_len == 0:
            raise Exception("'" + key + "' is not a valid format for the chapter key.")
        
        elif split_key_len == 2:
            return int(split_key[0]) * 10 + int(split_key[1])
        
        else:
            return int(split_key[0]) * 10

# define high_rain_volume = Image("high_rain_volume")
# define med_rain_volume = Image("med_rain_volume")
# define low_rain_volume = Image("low_rain_volume")


# define current_rain_volume = high_rain_volume

define words_seen_dictionary = ""

init -2 python:

    @renpy.pure
    class SetPreferencesDefault(Action):        
        
        def __init__(self, page=None, confirm=True):
            self.page = page
            self.confirm = confirm
        
        def __call__(self):
            
            func = None
            msg = ""
            
            if self.page:
                
                if self.page == "system":
                    func = SetPreferencesDefault.set_system
                
                elif self.page == "sound":
                    func = SetPreferencesDefault.set_sound
                
                else:
                    raise Exception("'" + self.page + "' is not a valid value.")
                
                msg = _("このページの環境設定を初期化しますか？")
            
            else:
                func = SetPreferencesDefault.set_all
                msg = _("Reset all settings to default?")
            
            
            if self.confirm:
                renpy.run(Confirm(msg, yes=func, no=None))
            else:
                func()
        
        @staticmethod
        def set_system():
            
            if config.default_fullscreen:
                renpy.run(Preference("display", "fullscreen"))
            else:
                renpy.run(Preference("display", "window"))
            
            persistent.window_opacity = config.window_opacity_default

            renpy.run(Preference("text speed", config.default_text_cps))
            
            renpy.run(Preference("auto-forward time", config.default_afm_time))
            
            renpy.run(Preference("skip", "seen"))
            
            if config.has_voice:
                renpy.run(Preference("wait for voice", "enable"))
        
        @staticmethod
        def set_sound():
            
            renpy.run(Preference("music volume", config.default_music_volume))
            
            renpy.run(Preference("mixer game_sfx volume", config.default_game_sfx_volume))

            renpy.run(Preference("sound volume", config.default_sfx_volume))
            
            if config.has_voice:
                renpy.run(Preference("voice mute", "disable"))
                
                renpy.run(Preference("voice volume", config.default_voice_volume))
                
                renpy.run(Preference("voice sustain", "disable"))
        
        @staticmethod
        def set_all():
            SetPreferencesDefault.set_system()
            SetPreferencesDefault.set_sound()

init -2 python:
    @renpy.pure
    class JumpDialogue(Action):        
        
        def __init__(self,func1, page=None, confirm=True):
            self.page = page
            self.confirm = confirm
            self.func1 = func1
        def __call__(self):
            
            func = None
            msg = ""
            
            if self.page:
                
                if self.page == "system":
                    func = JumpDialogue.set_system
                
                elif self.page == "sound":
                    func = JumpDialogue.set_sound
                
                else:
                    raise Exception("'" + self.page + "' is not a valid value.")
                
                msg = _("このページの環境設定を初期化しますか？")
            
            else:
                func = renpy.run(RollbackToIdentifier(self))
                msg = _("Restart the settings to you?")
            
            
            if self.confirm:
                renpy.run(Confirm(msg, yes=func, no=None))
            else:
                func()


init -2 python:

    if persistent.seen_chapters is None:
        persistent.seen_chapters = {}
    
    if persistent.window_opacity is None:
        persistent.window_opacity = config.window_opacity_default


init python:
    def run_action(action):
        try:
            for a in action:
                run_action(a)
        except TypeError, te:
            action()
    class Keymapper(renpy.Displayable):
        def __init__(self, vargs, child, **kwargs):
            super(Keymapper, self).__init__(**kwargs)
            self.child = child
            self.vargs = vargs
        def render(self, width, height, st, at):
            return renpy.render(self.child, width, height, st, at)
        def event(self, ev, x, y, st):
            for keysym, action in self.vargs:
                if renpy.map_event(ev, keysym):
                    run_action(action)
            self.child.event(ev, x, y, st)
        def visit(self):
            return [ self.child ]

    KeymapTransform = renpy.curry(Keymapper)

    class NoRollbackObj(NoRollback):
        def __init__(self):
            self.rollback_color_set = False
            self.just_loaded = False
            self.voice_count_done = True
            self.last_loaded_slot = None

    no_rollback = NoRollbackObj()





init -3 python:

    DELAY_FASTEST = 0.1
    DELAY_FAST = 0.2
    DELAY_NORMAL = 0.5
    DELAY_LONG = 1.0
    DELAY_LONGEST = 2.0

    renpy.const(DELAY_FASTEST)
    renpy.const(DELAY_FAST)
    renpy.const(DELAY_NORMAL)
    renpy.const(DELAY_LONG)
    renpy.const(DELAY_LONGEST)

init -3 python:

    def linear(t):
        return t    

    def ease(t):
        import math
        return 0.5 - math.cos(math.pi * t) / 2.0

    def easein(t):
        import math
        return math.cos((1.0 - t) * math.pi / 2.0)

    def easeout(t):
        import math
        return 1.0 - math.cos(t * math.pi / 2.0)

    def easeinback(t):
        return t * t *((BACK_S + 1) * t - BACK_S)

    def easeoutback(t):
        t -= 1
        return t * t * ((BACK_S + 1) * t + BACK_S) + 1

    def ComposedTransition(transition1, transition2=None, inbetween_color="#000", inbetween_time=DELAY_NORMAL):
        inbetween_image = Solid(color=inbetween_color)
        return MultipleTransition([False,
            transition1, inbetween_image,
            Pause(inbetween_time),
            inbetween_image, transition2 and transition2 or transition1,
            True])


