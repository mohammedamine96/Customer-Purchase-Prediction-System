
import math
import json
import os

def get_dataset():
    # Data from the json file
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'dataset.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: dataset.json not found.")
        return []

def get_ordinal_mappings():
    # Mapping values to 1, 2, 3 based on order/magnitude
    return {
        "age": {
            "<=30": 1,
            "31...40": 2,
            ">40": 3
        },
        "income": {
            "low": 1,
            "medium": 2,
            "high": 3
        },
        "student": {
            "no": 1,
            "yes": 2
        },
        "credit_rating": {
            "fair": 1,
            "excellent": 2
        }
    }

def to_ordinal_vector(instance, mappings):
    vector = []
    # Order: age, income, student, credit_rating
    for attr in ["age", "income", "student", "credit_rating"]:
        val = instance[attr]
        # Get the integer value from the mapping
        int_val = mappings[attr][val]
        vector.append(int_val)
    return vector

def calculate_cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
        
    return dot_product / (magnitude1 * magnitude2)



def main():
    data = get_dataset()
    mappings = get_ordinal_mappings()
    
    # New example to predict
    query = {
        "age": "<=30", 
        "income": "medium", 
        "student": "yes", 
        "credit_rating": "fair"
    }
    
    query_vector = to_ordinal_vector(query, mappings)
    
    print(f"Query Instance: {query}")
    print(f"Query Vector (Ordinal): {query_vector}")
    print("-" * 60)
    print(f"{'ID':<4} | {'Cosine Sim':<10} | {'Class':<10} | {'Vector'}")
    print("-" * 60)
    
    scored_data = []
    for row in data:
        row_vector = to_ordinal_vector(row, mappings)
        sim = calculate_cosine_similarity(row_vector, query_vector)
        
        scored_data.append({
            "id": row["id"],
            "similarity": sim,
            "buys_computer": row["buys_computer"],
            "vector": row_vector
        })
    
    # Sort by similarity descending
    scored_data.sort(key=lambda x: x["similarity"], reverse=True)
    
    k = 5
    neighbors = scored_data[:k]
    
    yes_count = 0
    no_count = 0
    
    for n in neighbors:
        print(f"{n['id']:<4} | {n['similarity']:<10.4f} | {n['buys_computer']:<10} | {n['vector']}")
        if n['buys_computer'] == 'yes':
            yes_count += 1
        else:
            no_count += 1
            
    print("-" * 60)
    print(f"Top {k} Neighbors Votes (Ordinal Cosine):")
    print(f"Yes: {yes_count}")
    print(f"No: {no_count}")
    
    prediction = "yes" if yes_count > no_count else "no"
    print(f"\nFinal Prediction for buys_computer: {prediction}")

if __name__ == "__main__":
    main()
