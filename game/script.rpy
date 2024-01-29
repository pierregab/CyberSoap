# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

init python:
    def eline_speaking_callback(event, **kwargs):
        if event == "begin":
            # Show Eline talking for 2 seconds when she begins speaking
            renpy.show("M talking for 2s")


image fond = "fond_resized4.png"
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

    return
