from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import spacy

app = Flask(__name__)
api = Api(app)
CORS(app)  # Enable CORS for all routes

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

def translate_to_sql(nl_query):
    # Parse the NL query using spaCy
    doc = nlp(nl_query)

    # Extract entities and keywords
    entities = [ent.text for ent in doc.ents]
    keywords = [token.text for token in doc if token.is_alpha]

    # 'public.viewership' with the actual schema and table name
    schema_and_table = 'public.viewership'

    # Create a simple SQL query based on entities, keywords, and the actual schema and table name
    sql_query = f"SELECT {', '.join(entities)} FROM {schema_and_table} WHERE {' AND '.join(keywords)}"

    return sql_query

# Placeholder function for generating visualizations 
def generate_visualization(sql_query):
    # Visualization generation logic here
    return {"visualization_type": "bar_chart", "data": [...]}

class NLtoSQL(Resource):
    def post(self):
        data = request.get_json()
        nl_query = data.get('nl_query')

        # Translate NL to SQL
        sql_query = translate_to_sql(nl_query)

        # Generate visualization
        visualization = generate_visualization(sql_query)

        response_data = {
            "sql_query": sql_query,
            "visualization": visualization
        }

        return jsonify(response_data)

api.add_resource(NLtoSQL, '/nl_to_sql')

if __name__ == '__main__':
    app.run(debug=True, port=5001)




