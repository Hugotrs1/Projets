# coding: utf-8

import cgi

print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>CS2 Skins.gg</title>
    <link rel="icon" type="image/png" href="https://ih1.redbubble.net/image.5273118024.5498/raf,360x360,075,t,fafafa:ca443f4786.jpg">
    <style>
        /* Style de l'arrière-plan */
        html {
            background-color: #636363;
            height: 100%;
        }

        /* Style de l'en-tête */
        h1 {
            text-align: center;
            color: white;
            width: 700px;
            border-radius: 1em;
            border: solid 2px #fff;
            background-color: #ffa500;
            padding: 10px;
            margin: 0.5em auto;
        }

        /* Style des titres */
        h2 {
            color: white;
            font-size: 30px;
            text-align: start;
        }

        /* Style de la zone de contenu */
        body {
            width: 1250px;
            margin: 8px auto 0 auto;
            border: solid 2px #ffa500;
            color: white;
            text-align: center;
        }

        /* Style du conteneur */
        div#content {
            overflow: hidden;
            position: relative;
            background-color: #1d2c49;
        }

        /* Style de l'image */
        img#image1 {
            width: 12%;
            position: absolute;
            left: 1090px;
            bottom: 230px;
        }

        /* Style du texte */
        p#texte1 {
            color: white;
            font-size: 25px;
            text-align: left
        }
        
        /* Style des champs de texte et du bouton */
        input[type="text"],
        input[type="number"] {
            width: 300px;
            padding: 10px;
            border: 1px solid #ffffff;
            border-radius: 5px;
            background-color: #ffa500;
            color: white;
        }

        /* Style du bouton */
        input[type="submit"] {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Style des étiquettes du formulaire */
        form label {
            display: inline-block;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div id="content">
        <!-- En-tête -->
        <h1>Quel skin CS2 te correspond ?</h1>
        <p id="texte1"><strong>&nbsp;Veuillez entrer un nom de skin parmi les suivants ainsi qu'un prix souhaité</strong><br>
        &nbsp;(L'orthographe doit être la même)<br>
        &nbsp;-"AK-47"&nbsp;-"M4A4"<br>
        &nbsp;-"M4A1-S"&nbsp;-"AWP"<br>
        &nbsp;-"Deagle"&nbsp;-"USP"<br>
        &nbsp;-"Karambit"&nbsp;-"M9 Baïyonette"<br>
        &nbsp;-"Butterfly"&nbsp;-"Stylet"<br>
        
        <strong>&nbsp;Si vous souhaitez voir tous les skins de la base de données veuillez inscrire "All"<br>
        &nbsp;dans le premier encadré ainsi que "0" dans le second</strong></p>


        <form method="post" action="result.py">
            <!-- Champ de texte pour le nom de l'arme -->
            <label for="nom_arme"><strong><font size="5">Nom de l'arme :</font></strong></label>
            <input type="text" name="nom_arme" id="nom_arme" required><br>

            <!-- Champ de texte pour le prix souhaité -->
            <label for="prix_souhaite"><strong><font size="5">Prix souhaité :&nbsp;&nbsp;</font></strong></label>
            <input type="number" name="prix_souhaite" id="prix_souhaite" required><br>

            <!-- Bouton de recherche -->
            <input type="submit" value="Rechercher">
        </form>

        <!-- Image -->
        <img id="image1" src="https://ih1.redbubble.net/image.5273118024.5498/raf,360x360,075,t,fafafa:ca443f4786.jpg" title="CS2">
    </div>
</body>
</html>
    """

print(html)