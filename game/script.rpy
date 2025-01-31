# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

init python:
    def eline_speaking_callback(event, **kwargs):
        if event == "begin":
            # Show Eline talking for 2 seconds when she begins speaking
            renpy.show("gerante talking for 2s")

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

image splash = "splash.png"

label splashscreen:
    scene black
    with Pause(0.5)

    show splash with Pixellate(2,8)
    with Pause(3)

    scene black with Pixellate(2,8)

    return


image fond = "fond_resized4.png"

image ruelle = "ruelle.png"

image computer_screen = "pc.png"

image computer_screen_off = "pc_off.png"

image image_overlay = "Ecran_filtre.png"

image star_animation :
    "gui/menu/anim_etoile/etoile1.png"
    pause 0.2
    "gui/menu/anim_etoile/etoile2.png"
    pause 0.2 
    "gui/menu/anim_etoile/etoile3.png"
    pause 0.2
    "gui/menu/anim_etoile/etoile4.png"
    repeat

image building_animation : 
    "gui/menu/lumiere_building/fond1.png"
    pause 1
    "gui/menu/lumiere_building/fond2.png"
    pause 1
    "gui/menu/lumiere_building/fond3.png"
    pause 1
    "gui/menu/lumiere_building/fond4.png"
    repeat

image cat_animation:
    "gui/menu/anim_chat/fond1.png"
    pause random_delay_for_cat_animation()
    "gui/menu/anim_chat/fond2.png"
    pause random_delay_for_cat_animation()
    "gui/menu/anim_chat/fond3.png"
    pause random_delay_for_cat_animation()
    "gui/menu/anim_chat/fond4.png"
    pause random_delay_for_cat_animation()
    repeat

image car_animation:
    "gui/menu/anim_voiture/fond1.png"
    pause 0.1
    "gui/menu/anim_voiture/fond2.png"
    pause 0.1
    "gui/menu/anim_voiture/fond3.png"
    pause 0.1
    "gui/menu/anim_voiture/fond4.png"
    pause 0.1
    "gui/menu/anim_voiture/fond5.png"
    pause 0.1
    "gui/menu/anim_voiture/fond6.png"
    pause 0.1
    "gui/menu/anim_voiture/fond7.png"
    pause 0.1
    "gui/menu/anim_voiture/fond8.png"
    pause 0.1
    "gui/menu/anim_voiture/fond9.png"
    pause 0.1
    "gui/menu/anim_voiture/fond10.png"
    pause 0.1
    "gui/menu/anim_voiture/fond11.png"
    pause 0.1
    "gui/menu/anim_voiture/fond12.png"
    pause 0.1
    "gui/menu/anim_voiture/fond13.png"
    pause 0.1
    "gui/menu/anim_voiture/fond14.png"
    pause 0.1
    "gui/menu/anim_voiture/fond15.png"
    pause 0.1
    "gui/menu/anim_voiture/fond16.png"
    pause 0.1
    "gui/menu/anim_voiture/fond17.png"
    pause 0.1
    "gui/menu/anim_voiture/fond18.png"
    pause 0.1
    "gui/menu/anim_voiture/fond19.png"
    pause 0.070
    "gui/menu/anim_voiture/fond20.png"
    pause 0.070
    "gui/menu/anim_voiture/fond21.png"
    pause 0.050
    "gui/menu/anim_voiture/fond22.png"
    pause 0.050
    "gui/menu/anim_voiture/fond23.png"
    # random delay between 10 and 30 seconds
    pause random_delay_for_car_animation()
    repeat

image rana_ruelle_animation:
    "images/Rana_ruelle/rana2.png"
    linear 0.5
    "images/Rana_ruelle/rana3.png"
    linear 0.5
    "images/Rana_ruelle/rana4.png"
    linear 0.2
    "images/Rana_ruelle/rana5.png"
    linear 0.2
    "images/Rana_ruelle/rana6.png"
    linear 0.2
    "images/Rana_ruelle/rana7.png"
    linear 1
    "images/Rana_ruelle/rana8.png"
    linear 0.2
    "images/Rana_ruelle/rana9.png"
    linear 0.2
    "images/Rana_ruelle/rana10.png"
    linear 0.2
    "images/Rana_ruelle/rana11.png"
    linear 0.2
    "images/Rana_ruelle/rana12.png"
    linear 1
    #"images/Rana_ruelle/rana13.png"
    #linear 1
    #"images/Rana_ruelle/rana13.png"
    #linear 1
    "images/Rana_ruelle/rana12.png"
    linear 2
    repeat

image cigarette_animation:
    xalign 0.5
    yalign 0.5
    "images/cigarette/red_ridge/cig2.png"
    pause 0.5
    "images/cigarette/red_ridge/cig3.png"
    pause 0.5
    "images/cigarette/red_ridge/cig4.png"
    pause 0.5
    "images/cigarette/red_ridge/cig5.png"
    pause 0.5
    "images/cigarette/red_ridge/cig6.png"
    pause 1
    repeat


layeredimage main_menu_animated:
    always:
        "gui/menu/main_fond/fond_resized.png"
    always:
        "car_animation"
    always:
        "star_animation"
    always:
        "cat_animation"
    always:
        "building_animation"

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

image Rana_speaking:
    yalign 0.54
    xalign 0.10
    "images/Rana_ruelle_speaking/Rana_2_speaking1.png"
    pause 0.2
    "images/Rana_ruelle_speaking/Rana_2_speaking2.png"
    pause 0.2
    "images/Rana_ruelle_speaking/Rana_2_speaking3.png"
    pause 0.2
    "images/Rana_ruelle_speaking/Rana_2_speaking2.png"
    pause 0.2
    "images/Rana_ruelle_speaking/Rana_2_speaking1.png"
    pause 0.2
    repeat 
    
    

image neko_fond = "NekoOS_fond.png"




# Define the animated image for 'M'
image gerante idle:
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

image gerante talk:
    yalign 0.042
    xalign 0.4
    "M1.png"
    pause .3  # Duration the mouth stays closed
    "M_b.png"
    pause .3  # Duration the mouth stays open
    repeat

image gerante talking for 2s:
    "gerante talk"  # This will play the talking animation
    pause 2.0  # Duration of talking
    "gerante idle"  # Switch back to idle animation after talking

image Rana :
    yalign 0.042
    xalign 0.75
    "louise2.png"


# Déclarez les personnages utilisés dans le jeu.
define gerante = Character('Eline', color="#612067", what_slow_cps=30, what_slow_abortable=True, callback=eline_speaking_callback)
define gerante_i = Character('???', color="#612067", what_slow_cps=30, what_slow_abortable=True, callback=eline_speaking_callback)
define gerante_i_hide = Character('???', color="#612067", what_slow_cps=30, what_slow_abortable=True)

define Rana = Character('Rana', color="#20675a", what_slow_cps=30, what_slow_abortable=True)
define Rana_i = Character('???', color="#20675a", what_slow_cps=30, what_slow_abortable=True)

define myself = Character('Alix', color="#53ddf3", what_slow_cps=30, what_slow_abortable=True)

define vox = Character('VOX', color="#f81717", what_slow_cps=30, what_slow_abortable=True)

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

    #imagebutton:
    #    idle "bouton_off.png"
    #   action Jump("pc_off")
    #    xpos 100
    #    ypos 900

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
        xpos 116
        ypos 728

    imagebutton:
        idle "menu_charger_button.png"
        action ShowMenu("load")
        xpos 116
        ypos 780

    imagebutton:
        idle "menu_stop_button.png"
        action Quit(confirm=True)
        xpos 116
        ypos 832

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

    #imagebutton:
    #    idle "bouton_off.png"
    #    action Jump("pc_off")
    #    xpos 100
    #    ypos 900

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



screen drink_order_buttons():
    window 
    zorder 1
    vbox:
        xalign 0.2
        yalign 0.9
        spacing 20
        text "Voulez-vous commander un verre ?" style "drink_menu_title"
        hbox:
            spacing 20
            textbutton "Yes" action Jump("order_drink_menu") style "choice_button"
            textbutton "No" action Jump("no_drink_order") style "choice_button"

style choice_button:
    background None
    hover_background "#3333334D"
    padding (20, 10)
    xminimum 100

style choice_button_text:
    color "#ffffff"
    hover_color "#cccccc"
    size 24

label order_drink_menu:
    hide screen drink_order_buttons
    scene black with pixellate
    $ selected_drink = renpy.call_screen("drink_selection")
    if selected_drink != "Cancel":
        "You ordered [selected_drink]."
    else:
        "You decided not to order anything."
    return

label no_drink_order:
    hide screen drink_order_buttons
    "You decide not to order a drink."
    return

screen drink_selection():
    modal True
    frame:
        background "black"
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text "Select a drink:" style "drink_menu_title"
            grid 2 3:
                spacing 10
                textbutton "Beer" action Return("Beer")
                textbutton "Wine" action Return("Wine")
                textbutton "Cocktail" action Return("Cocktail")
                textbutton "Soda" action Return("Soda")
                textbutton "Water" action Return("Water")
                textbutton "Coffee" action Return("Coffee")
            textbutton "Cancel" action Return("Cancel") xalign 0.5

style drink_menu_title:
    color "#ffffff"
    size 24
    xalign 0.5

label drink_selection_flow:
    call screen drink_order_buttons
    return

screen choice_menu1():
    zorder 100  # High zorder to ensure it's in front of everything
    vbox:
        xalign 0.2
        yalign 0.9  # Adjust the vertical position as needed
        spacing 20  # Adjust spacing between buttons

        textbutton "Aller fumer avec Rana":
            action Jump("smoke_with_rana")
            style "menu_choice_button"

        textbutton "Rester avec Eline":
            action Jump("stay_with_eline")
            style "menu_choice_button"

screen choice_menu2():
    zorder 100  # High zorder to ensure it's in front of everything
    vbox:
        xalign 0.2
        yalign 0.9  # Adjust the vertical position as needed
        spacing 20  # Adjust spacing between buttons

        textbutton "Qu’est ce que c’était ce flash info ? Tu crois qu’ils veulent vraiment limiter l’art ?":
            action Jump("rana_info_choice")
            style "menu_choice_button"

        textbutton "Tu vis ici depuis longtemps ?":
            action Jump("rana_small_talk")
            style "menu_choice_button"

style menu_choice_button:
    size_group "choice"
    xalign 0.5
    yalign 0.5
    background None
    hover_background "#3333334D"
    padding (10, 10)
    xminimum 300
    text_align 0

label rana_info_choice:

    myself "Qu’est ce que c’était ce flash info ? Tu crois qu’ils veulent vraiment limiter l’art ?"

    Rana "Ça a commencé avec des avertissements aux artistes les plus controversés, puis les médias ont gosthé de leurs plateformes tout ce qui pouvait être un peu trop piquant pour notre gouvernement et nos patrons."
    Rana "Des mots, des images, des sons effacés pour toujours de NSN. Et maintenant ils veulent aller plus loin, toujours plus loin, il veulent tout bannir."
    Rana "[nom entreprise divertissement] aura le monopole de la musique, du cinéma, de la photo, de la peinture… de l’art quoi."

    myself "C’est horrible ! Comment je vais faire pour écrire ?"

    Rana "Aha ne t’inquiètes pas, vu ton style je suis certaine que la [entreprise] pourrait accepter de te produire."
    Rana "Il te suffira de rester sage et de ne rien dire de méchant : comporte toi comme une enfant, ne dis jamais de gros mots ou sinon tes parents te mettrons au cachot !"

    myself "Et… si un jour je n’avais plus envie d'être sage ?"

    Rana "Alors il faudra faire comme pour toutes les crises d’ado ! Soit tu fugues, soit tu te rebelles contre les parents. Mais pour ça il faut déjà être prêt à se pendre des claques."

    return

label rana_small_talk:

    myself "Tu vis ici depuis longtemps ?"

    Rana "Depuis toujours. Dans cette ville quand tu naît ici, tu travailles ici et tu meurs ici. Que ce soit dans un bureau en haut d’un building ou au milieu des poubelles, tout le monde a le même destin pourri."

    myself "Tu as une triste vision de la vie…"
    
    Rana "Mais Alix c’est la réalité de Neo Stras."
    Rana "Ensuite si ce sont juste les lumières et les paillettes qui t'intéressent..."
    Rana "Si tu cherches juste à t’inspirer de la misère et de ses jolies couleurs sous les néons, si ton but c’est d'écrire des romans creux dont personne ne se souviendra jamais… alors j’imagine que tu t’y plairas."

    myself "Je ne comprends pas. Si tu hais tant cette ville, pourquoi ne pas partir ?"

    Rana "Tu crois qu’on peut toujours fuir ses problèmes ? Des fois il n’y a pas d’autre choix que de les affronter. Si j’abandonne cette ville, je m’abandonne moi même."

    return 

label smoke_with_rana:

    myself "Je peux t’accompagner ?"
    Rana "Euh oui si tu veux."

    # Hide all previously shown elements at once to prevent staggered hiding
    hide all

    # Hide the dialogue window to prevent the textbox from appearing
    window hide

    # Show cigarette animation on black screen
    scene black with dissolve
    show cigarette_animation  # Make sure this image is defined
    with Pause(3.0)  # Let animation play briefly before dialogue

    
    # Show the dialogue window again
    window show

    # Replace 'fond' with 'ruelle' using a dissolve transition
    scene ruelle:
        ypos -0.25
        xalign 0.5
    with dissolve

    show rana_ruelle_animation:
        yalign 0.54
        xalign 0.10

    pause 4.5

    # Passer à l'image de Rana en train de parler
    hide rana_ruelle_animation
    show Rana_speaking

    Rana "Alors, Alix, quelles sont tes premières impressions de Neo Stras ?"

    # Revenir à l'animation après le dialogue
    hide Rana_speaking
    show rana_ruelle_animation:
        yalign 0.54
        xalign 0.10

    myself "Oh je viens d’arriver, j’ai pas encore vu grand chose. J’aime bien les lumières de la ville la nuit, l’impression qu’elle dort jamais. Ce quartier est un peu plus… sombre."

    # Passer à l'image de Rana en train de parler
    hide rana_ruelle_animation
    show Rana_speaking

    Rana "Oui j’imagine qu’on peut y trouver un certain charme."

    hide Rana_speaking
    show rana_ruelle_animation:
        yalign 0.54
        xalign 0.10

    call screen choice_menu2

    # Continue with the storyline where the player goes to smoke with Rana.
    # Jump back to the main story after this choice
    jump after_choice


label stay_with_eline:
    # This label handles the scenario where the player chooses to stay with Eline.
    
    hide Rana with fade 

    vox "L’insecurité qui sévit dans les rues de notre belle ville saura être combattu à sa source grâce à cette loi."
    vox "La entreprise pour l’ordre sera à votre côté pour faire le ménage parmis les artistes qui veulent nuit à notre société."
    vox "Elle remettra à l’ordre tous les fauteurs de trouble, les mésinformateurs, des petits délinquants du graphiti jusqu’aux organisation d’artistes anarchistes qui se prennent pour la mafia !"

    gerante "Je vais baisser le son."

    myself "Ça fait peur cette histoire…"

    gerante "Non ne t’inquiètes pas. C’est toujours pareil : de grands mots pour pas grand chose. Au final rien ne change vraiment jamais tu sais. C’est juste du vent la politique."

    myself "Si vous le dites."

    gerante "Je t’en prie Alix, ne me vouvoie pas ! Je ne suis pas si vieille que ça. Et puis tu sais, une fois que tu mets un pied dans ce bar tu fais partie de la famille."

    myself "Comment ça ? C’est une sorte de… secte ?"

    gerante "Ahaha non non ne t’inquiètes pas. C’est juste que tu ne connais personne dans cette ville, mais si tu souhaites revenir ici alors tu ne seras jamais seule."
    gerante "Tu auras tous les soirs des amis devant et derrière le bar."

    myself "Tu as l’air de beaucoup apprécier cet endroit."

    gerante "Évidemment, c’est moi la gérante ! Le Yofukashi c'est mon bébé, mon bijou. Mes employés sont comme les membres de ma famille et les clients sont mes plus proches amis."
    gerante "Ici ils pleurent dans mes bras, ils rient à en réveiller les voisins, parfois ils boivent pour oublier, parfois pour rendre la nuit mémorable."
    gerante "Chaque soir est un spectacle, une histoire ou une confidence, et moi je veille sur ce petit royaume de la nuit."
    gerante "Mais ce soir tu es la seule qui est venue Alix ! Alors ça fait de toi… ma seule amie. Et tu sais ce que font les amies entre elles ? Elles se racontent tout !"
    
    myself "Euh… Eline je…"

    gerante "Quels sont tes secrets Alix ? Je te promets que je ne les répéterai à personne…"

    show Rana:
        yalign 0.067
        xalign 0.75

    gerante "Rana vas t’en j'étais en pleine discussion avec Alix, c'est très important !"

    Rana "Hein ?"

    myself "Merci Eline pour toutes ces belles explications mais il est tard je dois rentrer. Demain je commence à écrire et je veux me lever tôt. Bonne soirée !"

    gerante "Oh non déjà ? Tu reviens demain ?"

    myself "... Oui. À demain."

    # Jump back to the main story after this choice
    jump after_choice

# Le jeu commence ici
label start:
    window show
    show main_menu_animated:
        ypos +0.0005

    myself "C’est… ici ? Est ce que c’est une blague ?"
    myself "Une ruelle sombre et un bar glauque… Super. Je suppose que c’est là que je dois récupérer mes clés."
    myself "J’espère qu’ils sont pas trop bruyants, je vais être juste au dessus et il faut que je me concentre sur mes projets d’écriture…"
    myself "..."
    myself "Alors c’est ça ma nouvelle vie."

    hide main_menu_animated

    Rana_i "Je m’ennuieeeee…"
    gerante_i_hide"Ce genre de soir me ruine le moral, même nos clients les plus fidèles n’ont pas daignés sortir."
    Rana_i "On a déjà nettoyé le lave verre ?"
    gerante_i_hide "Trois fois."


    with pixellate
    scene fond

    show gerante idle:
        yalign 0.042
        xalign 0.4
    show Rana :
        yalign 0.067
        xalign 0.75
    
    gerante_i "BONSOIR !!!"

    myself "Euh bonsoir. Je viens récupérer les clés pour l’appartement du dessus."

    gerante_i "Ah."
    gerante_i "Tu veux boire quelque chose ?"

    myself "Euh..."

    gerante_i "C’est moi qui offre ! Ca nous ferai plaisir d’avoir quelqu’un avec nous ce soir, surtout si c’est une nouvelle tête !"

    myself "Bon… Si c’est gratuit…"
    
    window hide

    # Call the drink selection flow
    call drink_selection_flow

    window show
    scene fond

    show gerante idle:
        yalign 0.042
        xalign 0.4
    show Rana :
        yalign 0.067
        xalign 0.75

    gerante "Moi c’est Eline, et elle c’est Rana. Bienvenu au Yofukashi !"
    Rana "Yo."

    myself "Enchantée. Alix."

    gerante "Alors Alix, dis moi : qu’est ce que tu viens faire à Néo Stras ?"

    myself "Je viens pour écrire. J’ai vécu longtemps chez mes parents et j’y ai écrit mon premier livre."
    myself "Comme ça m'a rapporté un peu d’argent, j’avais envie de changer d’air, trouver de nouvelles inspirations pour continuer là dedans."

    Rana "C’est quoi le livre ?"

    myself "Amour silicone."

    Rana "Hm."

    myself "Tu connais ?"

    Rana "Non, je me suis arrêtée à la lecture du résumé. Ça avait l’air niais et vide et … "

    gerante "Une écrivaine à mon bar ! Quel honneur ! Je suis sûre que ton roman est super. N’est ce pas Rana ?"

    Rana "Ah, euh, oui bien sûr."

    vox "VOX interrompt votre programme de divertissement pour un flash info."
    vox "Vos représentants Neo Strassiens étudient actuellement à l’assemblée démocratique la proposition de loi de *nom entreprise divertissement* afin d’encadrer la production artistique déviante et haineuse."

    Rana "...connards..."

    Rana "Je vais fumer."

    # Display the choice menu
    call screen choice_menu1

    return

# Define a label to continue the main story after the choice
label after_choice:
    with fade

    window hide

    # Continue the story after drink selection
    scene computer_screen_off at offset_y with fade
    show screen loading
    # Use the total_loading_duration for the pause
    pause(total_loading_duration)
    hide screen loading

    scene computer_screen at offset_y
    call screen pc

    pause

    return
