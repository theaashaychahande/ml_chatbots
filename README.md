# AI Chatbot with Machine Learning

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![ML](https://img.shields.io/badge/Machine-Learning-orange.svg)
![Chatbot](https://img.shields.io/badge/Type-Chatbot-green.svg)

A conversational AI chatbot that learns from interactions using TF-IDF vectorization and cosine similarity for contextual responses.

## Features

- **Natural Language Processing**: Basic NLP capabilities for understanding user input
- **Emotion Detection**: Identifies user emotions (happy, sad, angry, neutral)
- **Machine Learning Responses**: Uses TF-IDF and cosine similarity to find contextually appropriate responses
- **Conversation Memory**: Stores chat history in JSON format for continuous learning
- **Colorful Interface**: Color-coded console output for better user experience
- **Contextual Understanding**: Maintains context through conversation history

## How It Works

### Core Technologies

1. **TF-IDF Vectorization**: Converts conversations into numerical vectors
2. **Cosine Similarity**: Measures similarity between current input and past conversations
3. **Rule-Based Responses**: Handles common phrases (greetings, goodbyes, etc.)
4. **Emotion Detection**: Simple keyword-based emotion classification

### Workflow

1. User inputs text message
2. System checks for:
   - Standard greetings/goodbyes
   - Emotional keywords
   - Previous similar conversations
3. For novel inputs:
   - Stores the new interaction
   - Responds generically while learning
4. For familiar inputs:
   - Retrieves most similar past response
   - Returns contextually appropriate answer

