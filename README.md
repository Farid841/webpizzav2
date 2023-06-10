# Pizza

Ce projet est un exemple de projet Django pour Pizza.

## Prérequis

Avant d'installer et d'exécuter le projet, assurez-vous d'avoir les éléments suivants :

- Python 3.8 ou version ultérieure
- pip (le gestionnaire de packages Python)

## Installation

Suivez ces étapes pour installer et exécuter le projet :

1. Clonez le référentiel GitHub :



2. Accédez au répertoire du projet :

```
     cd webpizzav2
 ```


3. Créez un environnement virtuel pour isoler les dépendances Python :

 ```
     python3 -m venv venv
 ```


4. Activez l'environnement virtuel :

   - Sur macOS et Linux :

     ```
     source venv/bin/activate
     ```

   - Sur Windows :

     ```
     venv\Scripts\activate
     ```


5. Installez les dépendances du projet à l'aide de pip :

   ```
     pip install -r requirements.txt
   ```


6. Effectuez les migrations de la base de données :

    ```
        python manage.py migrate
    ```


7. Lancez le serveur de développement :

    ```
        python manage.py runserver
    ```


8. Accédez à l'URL suivante dans votre navigateur :

    ```
        http://localhost:8000/
    ```


9. Vous devriez maintenant voir l'application en cours d'exécution localement sur votre machine.