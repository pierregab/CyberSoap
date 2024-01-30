# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

init python:
    def eline_speaking_callback(event, **kwargs):
        if event == "begin":
            # Show Eline talking for 2 seconds when she begins speaking
            renpy.show("M talking for 2s")


image fond = "fond_resized4.png"

image computer_screen = "pc.png"

image image_overlay = "Ecran_filtre.png"

transform offset_y:
    yoffset -5  # Replace 100 with the number of pixels you want to offset by


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


screen news_app():
    # Utilisez frame pour l'arrière-plan du menu de l'application

    frame:

        background "Capitimefenetre.png"
        
        # Utilisez viewport à l'intérieur du frame pour la partie défilable
        viewport:
            xpos 103
            ypos 289
            xsize 1300
            ysize 640
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
            ypos 111




screen pc :
    imagebutton:
        idle "Apli_2.png"
        action Jump("email_app")
        xpos 1100
        ypos 200
    
    imagebutton:
        idle "Apli_1.png"
        action Jump("time_app")
        xpos 1100
        ypos 450

    imagebutton:
        idle "Apli_3.png"
        action Jump("love_app")
        xpos 1100
        ypos 700

    add "Ecran_filtre.png" at offset_y


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

    scene computer_screen at offset_y with fade
    call screen pc

    pause



    return
