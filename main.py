def categorize_task(task):
    task = task.lower()
    # Mots-clés pour la catégorisation
    if "étude" in task or "lire" in task or "recherche" in task:
        return "Étude"
    elif "acheter" in task or "magasin" in task:
        return "Personnel"
    else:
        return "Général"

def save_task(task, category):
    # Enregistrement dans le fichier texte
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(f"Tâche: {task} | Catégorie: {category}\n")
    print("Tâche enregistrée avec succès !")

def main():
    print("--- Bienvenue dans le Smart Task Manager ---")
    while True:
        task = input("Entrez votre tâche (ou tapez 'quitter' pour arrêter) : ")
        if task.lower() == 'quitter':
            break
        
        category = categorize_task(task)
        print(f"Tâche catégorisée comme : {category}")
        save_task(task, category)

if __name__ == "__main__":
    main()