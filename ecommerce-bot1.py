from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# Configure Groq API
client = Groq(api_key='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')

conversation_state = {}
# List of eCommerce-related keywords
ecommerce_keywords = [
    "product", "order", "delivery", "shipping", "payment", "checkout", "cart", "discount",
    "price", "quantity", "return", "exchange", "customer service", "track", "availability",
    "size", "color", "specifications", "reviews", "feedback", "refund", "confirmation",
    "items", "promotions", "offers", "coupons", "support", "invoice", "payment method",
    "credit card", "debit card", "paypal", "netbanking", "order status", "order history",
    "wishlist", "favorite", "search", "category", "new arrivals", "sale"
]

def generate_response(user_input):
    ecommerce_context = (
        "You are a virtual assistant for an eCommerce platform. "
        "Help the user by prompting them to choose from a variety of products, "
        "ask for their price range, delivery address, and finally confirm their order. "
        "Make sure to gather the following details: "
        "1. Product options: List various products such as electronics, clothing, accessories, etc. "
        "2. Price range: Ask for the minimum and maximum price they are willing to pay. "
        "3. Delivery address: Get the full address for shipping. "
        "4. Confirm the order by summarizing the details they provided. "
        "Ensure to respond in a friendly and engaging manner."
    )
    
    # Create the request data structure
    request_data = {
        "messages": [
            {"role": "system", "content": ecommerce_context},
            {"role": "user", "content": user_input}
        ],
        "model": "llama3-8b-8192"  # Ensure this is a valid model name
    }

    try:
        response = client.chat.completions.create(**request_data)
        return response.choices[0].message.content if response and response.choices else "I'm here to assist with eCommerce inquiries only."
    except Exception as e:
        print(f"Error: {e}")
        return "I'm here to assist with eCommerce inquiries only."

def is_ecommerce_related(user_input):
    return any(keyword.lower() in user_input.lower() for keyword in ecommerce_keywords)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    user_id = request.json.get('id')

    if user_id not in conversation_state:
        conversation_state[user_id] = {'order': {}}

    if not is_ecommerce_related(user_input):
        return jsonify({"response": "I'm here to assist with eCommerce inquiries only."})

    response = generate_response(user_input)
   
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
