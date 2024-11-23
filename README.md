# Personal Fitness Tool

The **Personal Fitness Tool** is a comprehensive application designed to help users manage their personal fitness journey. It combines AI-generated insights, goal tracking, and data storage to provide a seamless experience for maintaining and improving health and fitness.

## Purpose
The purpose of this application is to provide users with an intuitive platform to:
- Input and manage personal health data such as name, age, weight, height, and activity level.
- Set fitness goals like muscle gain, fat loss, or staying active.
- Generate customized nutritional macros using AI based on their profile and goals.
- Ask AI for guidance on fitness-related topics.
- Store and manage fitness notes to track progress or important information.

## Key Features
1. **Personal Data Management**
   - Allows users to input and edit personal health data.
   - Tracks data such as weight, height, age, gender, and activity levels.

2. **Fitness Goal Setting**
   - Users can set and save specific fitness goals.
   - Goals are used to tailor recommendations and macros.

3. **AI-Generated Nutritional Macros**
   - Uses AI to calculate the ideal nutritional intake based on user profile and fitness goals.
   - Provides calorie, protein, fat, and carbohydrate recommendations.

4. **AI-Driven Q&A**
   - Users can ask fitness-related questions to an AI for guidance.
   - AI provides detailed, tailored responses.

5. **Notes Management**
   - Users can add, view, and delete notes related to their fitness journey.
   - Notes are stored in the database for future reference.

## How It Works
1. **Personal Profile**
   - Users input their personal data such as name, age, weight, height, gender, and activity level.
   - Data is stored securely in a database and is used to customize recommendations.

2. **Goal Setting**
   - Users select fitness goals, which are used to tailor AI-generated recommendations.

3. **Macros Calculation**
   - Users click a button to generate nutritional macros using AI.
   - The AI uses the stored personal profile and goals to calculate ideal calorie, protein, fat, and carbohydrate values.

4. **AI Interaction**
   - Users can ask the AI questions for fitness advice or guidance.
   - The AI responds with detailed, actionable insights.

5. **Notes**
   - Users can add notes to track progress, store reminders, or record thoughts.
   - Notes can be edited or deleted as needed.

## Project Structure
The application consists of the following files:

1. **`ai.py`**  
   Handles interaction with the LangFlow API for AI functionalities like generating macros and answering questions.

2. **`db.py`**  
   Manages interactions with the Astra DB database, including creating and managing collections for personal data and notes.

3. **`form_submit.py`**  
   Provides utility functions to update personal information and manage notes.

4. **`main.py`**  
   The main Streamlit application, which integrates all components into a user interface.

5. **`profiles.py`**  
   Contains functions to create, retrieve, and manage user profiles and associated data.

6. **`.env` File**  
   Stores sensitive credentials such as API tokens and database endpoints.

## Requirements
- Python 3.8+
- Streamlit
- Requests
- Astrapy
- dotenv

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hamzaabbasi16/workout_ask_ai.git
   cd workout_ask_ai
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   - Create a `.env` file in the project root with the following content:
     ```
     LANGFLOW_TOKEN=<your-langflow-token>
     ASTRA_ENDPOINT=<your-astra-db-endpoint>
     ASTRA_DB_APPLICATION_TOKEN=<your-astra-db-token>
     ```

4. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage
1. Open the application in your browser at the default Streamlit URL (e.g., `http://localhost:8501`).
2. Fill in your personal data and save it.
3. Set your fitness goals and generate macros using AI.
4. Use the "Ask AI" feature to get answers to fitness-related questions.
5. Add and manage notes to track your progress.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! If you encounter bugs or have suggestions for improvement, feel free to create an issue or submit a pull request.

---

Enjoy your fitness journey with the **Personal Fitness Tool**! 💪