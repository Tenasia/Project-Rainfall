﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Rainfall")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Rainfall"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = audio.rainfall

# define config.fade_music = 1.0
define config.main_menu_music = audio.rainfall


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.
init -2 python:

    ### Transition ###########
    config.enter_transition = Dissolve(.3)
    config.exit_transition = Dissolve(.3)
    # config.intra_transition = None


    ### Sounds ##########
    config.default_music_volume = 0.50
    config.default_sfx_volume = 0.50
    config.fade_music = 1.0
    



init -1 python hide:
    config.window_show_transition = Dissolve(.2)


    config.window_hide_transition = config.window_show_transition

    config.label_overrides = {"_hide_windows" : "_hide_windows_override"}

    config.after_load_transition = ComposedTransition(Dissolve(2.0))

    config.default_fullscreen = True

    config.game_main_transition = ComposedTransition(Dissolve(2.0))

    config.default_afm_time = 5


## Between screens of the game menu.

define config.intra_transition = None


## A transition that is used after a game has been loaded.

# define config.after_load_transition = None


    # config.window_show_transition = Dissolve(.2)
    # config.window_hide_transition = config.window_show_transition
    
    # config.message_alpha_default = 1.0
# # define config.window_hide_transition = True


## Used when entering the main menu after the game has ended.

# define config.end_game_transition = Dissolve(0.3)

## Used when entering the main menu after the splashscreen


define config.end_splash_transition = ImageDissolve("images/transitions/rain1.jpg", 1.0, 8)
# define config.end_splash_transition = None
## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window


# define config.window_show_transition = Dissolve(0.2)
# define config.window_hide_transition = Dissolve(0.2)

# init -1 python hide:
    

## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

# default preferences.afm_time = 10


# define config.save_directory = "BellumPerpetuumv3-1640259307"
define config.save_directory = "Rainfall"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


init python:


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

init -2 python:
    renpy.music.register_channel("music", mixer="music", loop = True, file_prefix="audio/bgm/", file_suffix=".mp3")
    renpy.music.register_channel("se1", mixer="game_sfx", loop = False, file_prefix="audio/gsfx/ogg/se/", file_suffix=".ogg")
    renpy.music.register_channel("se2", mixer="game_sfx", loop = False, file_prefix="audio/gsfx/ogg/se/", file_suffix=".ogg")
    renpy.music.register_channel("ambient", mixer="game_sfx", loop=True, file_prefix="audio/gsfx/ogg/ambient/", file_suffix=".ogg", tight=True)
init -1500 python:
    config.window_opacity_default = 0.85
    config.default_game_sfx_volume = 0.50

    