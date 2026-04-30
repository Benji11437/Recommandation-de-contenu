# Realisez-une-application-de-recommandation-de-contenu

Système de recommandation hybride – Filtrage de contenu - collaboratif & Modèles implicites

### Présentation du projet
Ce projet implémente un système de recommandation d’articles d’actualité de bout en bout, basé sur plusieurs approches complémentaires du machine learning.
L’objectif est de proposer des recommandations personnalisées en exploitant à la fois :
•	le contenu des articles (embeddings) 
•	le comportement des utilisateurs (clics) 
•	les interactions implicites

 ### Approches utilisées
1. Filtrage basé sur le contenu (Content-Based Filtering)
•	Utilisation des embeddings d’articles 
•	Construction d’un profil utilisateur pondéré 
•	Calcul de similarité (cosine similarity) 
•	Recommandation d’articles similaires à ceux déjà consultés

2. Filtrage collaboratif (SVD++)
•	Modèle basé sur la librairie Surprise 
•	Apprentissage des facteurs latents utilisateurs / articles 
•	Exploitation des interactions implicites (clics) 
•	Optimisation via RMSE

3. Modèles implicites de factorisation matricielle
•	ALS (Alternating Least Squares) 
•	BPR (Bayesian Personalized Ranking) 
•	LMF (Logistic Matrix Factorization) 
•	Utilisation de matrices creuses utilisateur–article

4. Modèle hybride
•	Combinaison du filtrage de contenu et collaboratif 
•	Fusion pondérée des scores 
•	Amélioration de la pertinence des recommandations
 
### Évaluation des modèles
Les performances sont évaluées à l’aide de plusieurs métriques :
•	RMSE (SVD++) 
•	Precision@K 
•	MAP@K (Mean Average Precision) 
•	nDCG@K (qualité de classement)

### Évaluation des modèles
Les performances sont évaluées à l’aide de plusieurs métriques :
•	RMSE (SVD++) 
•	Precision@K 
•	MAP@K (Mean Average Precision) 
•	nDCG@K (qualité de classement)


### Stack technique
•	Python 
•	Pandas / NumPy 
•	Scikit-learn 
•	Surprise 
•	Implicit 
•	SciPy 
•	Matplotlib

Architecture du projet
•	src/

 ├── data_loader.py
 
 ├── preprocessing.py
 
 ├── content_based.py
 
 ├── collaborative.py
 
 ├── implicit_models.py
 
 ├── hybrid.py
 
 ├── utils.py

main.py

### Résultats
Le modèle hybride améliore la qualité des recommandations en combinant :
•	la similarité sémantique des articles 
•	les comportements utilisateurs 
•	les interactions implicites

### Points forts du projet
•	Pipeline complet de recommandation 
•	Gestion des interactions implicites (clics) 
•	Approche hybride (content + collaborative) 
•	Architecture modulaire et réutilisable 
•	Compatible avec un déploiement en production

### Conclusion
Ce projet reproduit un système de recommandation proche des architectures industrielles, combinant plusieurs approches du machine learning pour améliorer la personnalisation des recommandations.
