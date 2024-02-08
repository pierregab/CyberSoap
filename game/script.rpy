# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

init python:
    def eline_speaking_callback(event, **kwargs):
        if event == "begin":
            # Show Eline talking for 2 seconds when she begins speaking
            renpy.show("M talking for 2s")

init python:
    # Initialize a global variable to store the total duration
    total_loading_duration = 0
    number_of_reset = 1

    def increase_number_of_reset():
        global number_of_reset
        number_of_reset += 1

    def random_delay():
        global number_of_reset
        # Randomly choose a number of seconds between, say, 0.1 to 1 seconds
        if number_of_reset > 0:
            reset_total_loading_duration()
            number_of_reset = 0
        delay_time = 0.1 * random.randint(1, 4)
        global total_loading_duration
        total_loading_duration += delay_time
        return delay_time

    def reset_total_loading_duration():
        global total_loading_duration
        total_loading_duration = 0


image fond = "fond_resized4.png"

image computer_screen = "pc.png"

image computer_screen_off = "pc_off.png"

image image_overlay = "Ecran_filtre.png"

transform offset_y:
    yoffset -5  # Replace 100 with the number of pixels you want to offset by

transform offset_neko:
    xoffset 540
    yoffset 380


image Neko_running:
    crop (0, 0, 480, 480)
    "NekoOS.png"   # First frame
    pause 0.1
    crop (480, 0, 480, 480)
    "NekoOS.png"   # Second frame
    pause 0.1
    crop (960, 0, 480, 480)
    "NekoOS.png"   # Third frame
    pause 0.1
    crop (1440, 0, 480, 480)
    "NekoOS.png"   # Fourth frame
    pause 0.1
    crop (1920, 0, 480, 480)
    "NekoOS.png"   # Fifth frame
    pause 0.1
    crop (2400, 0, 480, 480)
    "NekoOS.png"   # Sixth frame
    pause 0.1
    crop (2880, 0, 480, 480)
    "NekoOS.png"   # Seventh frame
    pause 0.1
    crop (3360, 0, 480, 480)
    "NekoOS.png"   # Eighth frame
    pause 0.1
    crop (3840, 0, 480, 480)
    "NekoOS.png"   # Ninth frame
    pause 0.1
    crop (4320, 0, 480, 480)
    "NekoOS.png"   # Tenth frame
    pause 0.1
    crop (4800, 0, 480, 480)
    "NekoOS.png"   # Eleventh frame
    pause 0.1
    crop (5280, 0, 480, 480)
    "NekoOS.png"   # Twelfth frame
    pause 0.1
    repeat

image Neko_loading:
    crop (0, 0, 480, 480)
    "NekoOS_loading.png"   # First frame
    pause random_delay()
    crop (480, 0, 480, 480)
    "NekoOS_loading.png"   # Second frame
    pause random_delay()
    crop (960, 0, 480, 480)
    "NekoOS_loading.png"   # Third frame
    pause random_delay()
    crop (1440, 0, 480, 480)
    "NekoOS_loading.png"   # Fourth frame
    pause random_delay()
    crop (1920, 0, 480, 480)
    "NekoOS_loading.png"   # Fifth frame
    pause random_delay()
    crop (2400, 0, 480, 480)
    "NekoOS_loading.png"   # Sixth frame
    pause random_delay()
    crop (2880, 0, 480, 480)
    "NekoOS_loading.png"   # Seventh frame
    pause random_delay()
    crop (3360, 0, 480, 480)
    "NekoOS_loading.png"   # Eighth frame
    pause random_delay()
    crop (3840, 0, 480, 480)
    "NekoOS_loading.png"   # Ninth frame
    pause random_delay()
    crop (4320, 0, 480, 480)
    "NekoOS_loading.png"   # Tenth frame
    pause random_delay()
    crop (4800, 0, 480, 480)
    "NekoOS_loading.png"   # Eleventh frame
    pause random_delay()
    crop (5280, 0, 480, 480)
    "NekoOS_loading.png"   # Twelfth frame
    pause random_delay()
    crop (5760, 0, 480, 480)
    "NekoOS_loading.png"   # Thirteenth frame
    pause random_delay()
    crop (6240, 0, 480, 480)
    "NekoOS_loading.png"   # Fourteenth frame
    pause random_delay()
    crop (6720, 0, 480, 480)
    "NekoOS_loading.png"   # Fifteenth frame
    pause random_delay()
    crop (7200, 0, 480, 480)
    "NekoOS_loading.png"   # Sixteenth frame
    pause random_delay()
    crop (7680, 0, 480, 480)
    "NekoOS_loading.png"   # Seventeenth frame
    pause random_delay()
    crop (8160, 0, 480, 480)
    "NekoOS_loading.png"   # Eighteenth frame
    pause random_delay()
    crop (8640, 0, 480, 480)
    "NekoOS_loading.png"   # Nineteenth frame
    pause random_delay()
    crop (9120, 0, 480, 480)
    "NekoOS_loading.png"   # Twentieth frame
    # trigger the next scene 
    
    

image neko_fond = "NekoOS_fond.png"




# Define the animated image for 'M'
image M idle:
    yalign 0.042
    xalign 0.4
    "M1.png"
    pause 2.5
    "M2.png"
    pause 0.3
    "M3.png"
    pause 0.3
    "M2.png"
    pause 0.3
    repeat

image M talk:
    yalign 0.042
    xalign 0.4
    "M1.png"
    pause .3  # Duration the mouth stays closed
    "M_b.png"
    pause .3  # Duration the mouth stays open
    repeat

image M talking for 2s:
    "M talk"  # This will play the talking animation
    pause 2.0  # Duration of talking
    "M idle"  # Switch back to idle animation after talking


# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eline', color="#612067", what_slow_cps=30, what_slow_abortable=False, callback=eline_speaking_callback)


label time_app:
    call screen news_app
    return

label pc:
    scene computer_screen at offset_y 
    call screen pc
    return

label start_menu:
    call screen start_menu
    return

screen start_menu:
    zorder 1
    add "start_menu.png"
    imagebutton:
        idle "Apli_2.png"
        action Jump("email_app")
        xpos 1200
        ypos 120
    
    imagebutton:
        idle "Apli_1.png"
        action Jump("time_app")
        xpos 1200
        ypos 320

    imagebutton:
        idle "Apli_3.png"
        action Jump("love_app")
        xpos 1200
        ypos 520

    imagebutton:
        idle "bouton_off.png"
        action Jump("pc_off")
        xpos 100
        ypos 900

    add "Ecran_filtre.png" at offset_y
    add "b_ta.png" at offset_y

    imagebutton:
        idle "start_button_idle.png"
        hover "start_button_hover.png"
        clicked "start_button_clicked.png"
        action Jump("pc")
        xpos 116
        ypos 890
    
    imagebutton:
        idle "menu_sauver_button.png"
        action ShowMenu("save")

screen news_app():
    # Utilisez frame pour l'arrière-plan du menu de l'application
    zorder 1

    frame:

        background "Capitimefenetre.png" at offset_y
        
        # Utilisez viewport à l'intérieur du frame pour la partie défilable
        viewport:
            xpos 113
            ypos 286
            xsize 1282
            ysize 648
            draggable True  # Permet au joueur de faire glisser pour défiler
            scrollbars "vertical"  # Défilement vertical seulement
            mousewheel True  # Défilement avec la molette de la souris
            arrowkeys True  # Défilement avec les touches fléchées
            
            # vpgrid pour la zone de contenu défilable
            vpgrid:
                cols 1
                rows 1

                # Ajoutez l'image de l'article de nouvelles ici
                add "Article_beta.png" at offset_y


    imagebutton:
            idle "bouton_quitter.png"
            action Jump("pc")
            xpos 1352
            ypos 109

label pc_off:
    scene computer_screen_off at offset_y
    call screen pc_off
    return

label loading:
    $ increase_number_of_reset()
    scene computer_screen_off at offset_y
    show screen loading
    pause(total_loading_duration)
    hide screen loading
    
    scene computer_screen at offset_y
    call screen pc
    return

screen pc_off :
    zorder 0
    imagebutton:
        idle "bouton_off.png"
        action Jump("loading")
        xpos 100
        ypos 900
        

    add "Ecran_filtre.png" at offset_y


screen pc :
    zorder 0
    imagebutton:
        idle "Apli_2.png"
        action Jump("email_app")
        xpos 1200
        ypos 120
    
    imagebutton:
        idle "Apli_1.png"
        action Jump("time_app")
        xpos 1200
        ypos 320

    imagebutton:
        idle "Apli_3.png"
        action Jump("love_app")
        xpos 1200
        ypos 520

    imagebutton:
        idle "bouton_off.png"
        action Jump("pc_off")
        xpos 100
        ypos 900

    add "Ecran_filtre.png" at offset_y
    add "b_ta.png" at offset_y

    imagebutton:
        idle "start_button_idle.png"
        hover "start_button_hover.png"
        clicked "start_button_clicked.png"
        action Jump("start_menu")
        xpos 116
        ypos 890

screen loading :
    zorder 0
    add "Ecran_filtre.png" at offset_y
    add "NekoOS_fond.png" at offset_neko
    add "Neko_running" at offset_neko
    add "Neko_loading" at offset_neko


# Le jeu commence ici
label start:


    window auto hide

    scene fond

    show M idle:
        yalign 0.042
        xalign 0.4

    with fade

    e "test"

    "testtttt"

    e "Bienvenue aux Cyber Savons !"


    scene computer_screen_off at offset_y with fade
    show screen loading
    # Use the total_loading_duration for the pause
    pause(total_loading_duration)
    hide screen loading

    scene computer_screen at offset_y
    call screen pc

    pause



    return
