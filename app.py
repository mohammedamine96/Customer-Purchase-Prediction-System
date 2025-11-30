from flask import Flask, render_template, request
import knn_solver

app = Flask(__name__)

def calculate_simple_matching(instance1, instance2):
    attributes = ["age", "income", "student", "credit_rating"]
    matches = []
    match_count = 0
    
    for attr in attributes:
        if instance1[attr] == instance2[attr]:
            matches.append('1')
            match_count += 1
        else:
            matches.append('0')
            
    similarity = match_count / len(attributes)
    return similarity, matches

@app.route('/')
def index():
    data = knn_solver.get_dataset()
    mappings = knn_solver.get_ordinal_mappings()
    
    # Get query from request args or use default
    query = {
        "age": request.args.get("age", "<=30"), 
        "income": request.args.get("income", "medium"), 
        "student": request.args.get("student", "yes"), 
        "credit_rating": request.args.get("credit_rating", "fair")
    }
    
    # 1. Cosine Similarity (Ordinal)
    # 1. Cosine Similarity (Ordinal)
    query_vector = knn_solver.to_ordinal_vector(query, mappings)
    cosine_results = []
    
    for row in data:
        row_vector = knn_solver.to_ordinal_vector(row, mappings)
        sim = knn_solver.calculate_cosine_similarity(row_vector, query_vector)
        cosine_results.append({
            "id": row["id"],
            "similarity": sim,
            "class": row["buys_computer"],
            "vector": row_vector
        })
    
    cosine_results.sort(key=lambda x: x["similarity"], reverse=True)
    cosine_top_k = cosine_results[:5]
    
    # 2. Simple Matching Similarity
    simple_results = []
    
    for row in data:
        sim, matches = calculate_simple_matching(row, query)
        simple_results.append({
            "id": row["id"],
            "similarity": sim,
            "class": row["buys_computer"],
            "matches": matches
        })
        
    simple_results.sort(key=lambda x: x["similarity"], reverse=True)
    simple_top_k = simple_results[:5]

    def get_prediction(neighbors):
        yes_count = sum(1 for n in neighbors if n['class'] == 'yes')
        no_count = sum(1 for n in neighbors if n['class'] == 'no')
        return "yes" if yes_count > no_count else "no"

    cosine_prediction = get_prediction(cosine_top_k)
    simple_prediction = get_prediction(simple_top_k)
    
    return render_template('index.html', 
                         query=query, 
                         cosine_results=cosine_top_k, 
                         simple_results=simple_top_k,
                         cosine_prediction=cosine_prediction,
                         simple_prediction=simple_prediction,
                         mappings=mappings)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
