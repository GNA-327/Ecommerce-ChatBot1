# Chatbot for eCommerce Assistance - README

This README provides instructions for setting up and running the Flask-based eCommerce chatbot.

## Steps to Set Up and Run the Chatbot

1. **Clone the Repository**
   - Open your terminal and run:
     ```
     git clone <repository-url>
     ```
   - Replace `<repository-url>` with the URL of your GitHub repository.

2. **Navigate to the Project Directory**
   - Change into the project directory:
     ```
     cd <your-project-directory>
     ```

3. **Create a Virtual Environment (optional but recommended)**
   - Create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```

4. **Install Required Packages**
   - Install Flask and the Groq library:
     ```
     pip install Flask groq
     ```

5. **Set Environment Variables**
   - Make sure to set your Groq API key in the code or as an environment variable.

6. **Run the Chatbot**
   - Ensure you're in the project directory and run:
     ```
     python app.py
     ```
   - The server will start at `http://127.0.0.1:5000/`.

## Testing with Postman

1. **Open Postman** and create a new request.

2. **Set the Request Type to `POST`** and enter the URL:

3. **Set Headers**:
- Click on the `Headers` tab and add:
  ```
  Key: Content-Type
  Value: application/json
  ```

4. **Set the Request Body**:
- Click on the `Body` tab, select `raw`, and choose `JSON`.
- Enter the following JSON:
  ```json
  {
    "message": "What products do you have?",
    "id": "user123"
  }
  ```

5. **Send the Request** and check the response from the chatbot.

## Usage

Interact with the chatbot using various eCommerce-related queries such as:
- "What products do you have?"
- "Track my order."
- "What are the payment options?"

