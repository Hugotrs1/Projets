# coding: utf-8

# Importation des modules requis
import cgi
import cgitb
import sqlite3

# Activation de la gestion des erreurs CGI
cgitb.enable()

# Extraction des données du formulaire
form = cgi.FieldStorage()
nom_arme = form.getvalue("nom_arme")
prix_souhaite = form.getvalue("prix_souhaite")

# Impression de l'en-tête HTTP
print("Content-type: text/html; charset=utf-8\n")

# Définition du code HTML de la page
html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>CS2 Skins.gg</title>
    <!-- Favicon de la page -->
    <link rel="icon" type="image/png" href="https://ih1.redbubble.net/image.5273118024.5498/raf,360x360,075,t,fafafa:ca443f4786.jpg">
    <style>
        /* Styles pour la page HTML */
        html {
            background-color: #636363; /* Couleur de fond générale (blanche) */
            height: 100%;
        }

        /* Styles pour le contenu principal */
        body {
            background-color: #1d2c49; /* Couleur de fond de la zone de contenu (grise) */
            width: 1250px;
            margin: 8px auto 0 auto;
            border: solid 2px #ffa500;
            color: #ffffff; /* Couleur du texte principal (blanc) */
            text-align: center;
        }

        /* Styles pour l'en-tête */
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
        p#texte1{
            text-align:left
        }
        /* Styles pour le tableau */
        .styled-table {
            border-collapse: collapse;
            width: 100%;
            font-family: Arial, sans-serif;
        }

        .styled-table thead th {
            background-color: #ffa500;
            color: #fff;
            text-align: center;
            padding: 10px;
        }

        .styled-table th,
        .styled-table td {
            padding: 8px 10px;
            border: 1px solid #ddd;
            text-align: center;
        }

        .styled-table tbody tr:nth-of-type(odd) {
            background-color: #1d2c49;
        }

        .styled-table tbody tr:hover {
            background-color: #ffa500;
        }
    </style>
</head>
<body>
    <h1> Résultats correspondant à """ + nom_arme + """</h1>
</body>
</html>
"""


try:
    # Connexion à la base de données SQLite
    conn = sqlite3.connect('data/biblioteque.db')
    c = conn.cursor()
    if nom_arme=="All" and prix_souhaite=="0" :
        c.execute("SELECT Armes, Rarete, Nom, Prix FROM Skins ORDER BY Prix")
    else:
    # Exécution de la requête SQL pour récupérer les données
        c.execute("SELECT Armes, Rarete, Nom, Prix FROM Skins WHERE Armes = ? AND Prix <= ? ORDER BY Prix", (nom_arme, prix_souhaite))
    
    # Récupération des résultats de la requête
    rows = c.fetchall()
    resultats = len(rows)
    html += "<p id=texte1>Nombre de résultats : {}</p>".format(resultats)
    print(html)
    # Création du tableau HTML pour afficher les résultats
    html = """
    <table class="styled-table">
        <thead>
            <tr>
                <th>Armes</th>
                <th>Rareté</th>
                <th>Nom</th>
                <th>Prix</th>
            </tr>
        </thead>
        <tbody>
    """ 
    for row in rows:
        html += "<tr>"
        for item in row:
            html += "<td>{}</td>".format(item)
        html += "</tr>"

    html += """
        </tbody>
    </table>
    """
    conn.commit()
    print(html)

except sqlite3.OperationalError as e:
    # Gestion des erreurs liées à la base de données
    html += "<p>Erreur de base de données : {}</p>".format(e)
except Exception as e:
    # Gestion des erreurs générales
    html += "<p>Erreur : {}</p>".format(e)
    conn.rollback()

# Fermeture de la connexion à la base de données
c.close()
conn.close()

# Finalisation de la page HTML
html += """
</body>
</html>
"""


