# Chaîne-de-Densité

Ce projet implémente l'approche de résumé textuel en chaîne-de-densité du document ["De Sparse à Dense: Résumé avec la Chaîne-de-Densité avec GPT-4"](https://arxiv.org/pdf/2309.04269.pdf) par des chercheurs de Salesforce, du MIT, de Columbia et d'autres.

La summarization en chaîne-de-densité est une nouvelle technique qui crée des résumés hautement condensés mais riches en informations à partir de textes longs. Elle fonctionne en extrayant de manière itérative des entités essentielles du texte source et en réécrivant le résumé pour incorporer plus d'entités à chaque étape (sans perdre les entités précédentes), résultant en une "chaîne" de résumés de plus en plus denses.

Cette implémentation prend une entrée de texte long (par exemple, des articles, des blogs, des livres blancs, des documents) et la soumet à plusieurs cycles d'extraction d'entités et de réécriture de résumé pour produire un résumé final dense contenant uniquement les informations critiques de la source.

Les principaux avantages de l'approche en chaîne-de-densité comprennent:

- Production de résumés fortement comprimés mais fidèles
- Capture des détails clés et des concepts à partir de textes complexes et longs
- Distillation itérative de la densité d'information
- Utilisation des capacités des grands modèles linguistiques pour la summarization

Ce référentiel fournit du code pour appliquer la summarization en chaîne-de-densité à des entrées de texte arbitraires en utilisant l'API OpenAI. Il extrait des entités, construit des prompts en chaîne-de-pensée, interroge l'API et produit des résumés condensés.

## Utilisation

Pour exécuter le summarizer:

1. Installez les dépendances:

```bash
poetry install 
```

2. Créez un fichier .env et définissez votre clé API OpenAI:

```bash
OPENAI_API_KEY=<votre-clé>
```

3. Mettez à jour config.ini avec le chemin du fichier texte d'entrée et l'emplacement de sortie.

4. Exécutez le summarizer: 

```bash
poetry run cod
```

Cela chargera le texte d'entrée, exécutera la summarization en chaîne-de-densité et sauvegardera le résultat dans le fichier configuré.

## Implémentation

La logique principale se trouve dans main.py. Il:

- Charge le texte d'entrée
- Obtient la clé API OpenAI du fichier .env  
- Envoie un prompt à l'API OpenAI avec le texte
- Reçoit en retour une chaîne de 5 résumés de plus en plus denses
- Exporte le résultat au format .txt

Le prompt suit largement la méthodologie décrite dans le document, à l'exception d'ajustements mineurs.

Les options de configuration comme les chemins d'entrée/sortie sont stockées dans config.ini.

## À faire

- Analyser la sortie au format JSON
- Compiler la liste des entités et des entités manquantes supplémentaires
- Permettre la fusion séquentielle et la summarization de plusieurs entrées
- Ajouter une critique de l'approche en chaîne-de-densité à la summarization (avantages et inconvénients)

## Références

- ["De Sparse à Dense: Résumé avec la Chaîne-de-Densité avec GPT-4"](https://arxiv.org/pdf/2309.04269.pdf)
- ["Résumés CoD annotés + non annotés sur Hugging Face"](https://huggingface.co/datasets/griffin/chain_of_density/)
- Génération de requirements.txt `poetry export --without-hashes -f requirements.txt --output requirements.txt`
