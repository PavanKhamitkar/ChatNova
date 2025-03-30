# ChatNova - Intelligent Conversational AI

## Problem Statement
In today's digital world, there's a growing need for intelligent conversational agents that can provide accurate, contextual responses while maintaining a natural flow of conversation. Traditional chatbots often lack sophistication and struggle with context maintenance, leading to unsatisfactory user experiences.

![ChatNova Interface](Screenshots/Screenshot%202025-03-30%20192237.png)

## How ChatNova Works
ChatNova is an advanced chatbot that leverages the power of Google's Gemini 1.5 Pro model to generate dynamic and contextually aware responses. The system:

- Maintains conversation history for contextual awareness
- Processes natural language queries in real-time
- Provides formatted responses with support for rich text
- Features text-to-speech capability with voice control
- Implements custom name recognition patterns


![ChatNova Interface](Screenshots/Screenshot%202025-03-30%20192657.png)

## Technologies Used
### Backend
- Python 3.x
- Flask web framework
- Google Generative AI (Gemini 1.5 Pro)
- Regular Expressions for pattern matching

### Frontend
- HTML5
- CSS3 with modern animations
- JavaScript for dynamic interactions
- Web Speech API for text-to-speech
- Responsive design principles

## Implementation Details
1. **API Integration**
   - Seamless integration with Google's Generative AI API
   - Streaming responses for better performance
   - Secure API key management

2. **User Interface**
   - Modern, dark-themed interface
   - Real-time message updates
   - Smooth animations and transitions
   - Mobile-responsive design

3. **Core Features**
   - Message streaming capability
   - Voice output with female voice preference
   - Message formatting support
   - Custom name recognition system

## Results and Impact
ChatNova demonstrates significant improvements in human-computer interaction:

- **Natural Conversations**: Maintains context and provides coherent responses
- **Accessibility**: Text-to-speech feature makes it accessible to more users
- **Performance**: Real-time response generation with minimal latency
- **User Experience**: Modern interface with intuitive controls
- **Scalability**: Built on reliable technologies for future expansion

## Getting Started
1. Clone the repository
2. Install required dependencies:
```bash
pip install flask google-generativeai
```
3. Replace the `GOOGLE_API_KEY` in `app.py` with your API key
4. Run the application:
```bash
python app.py
```

## Future Enhancements
- Multi-language support
- Voice input capability
- Enhanced formatting options
- Custom personality traits
- Response sentiment analysis


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Visit & Try ChatNova
- **GitHub Repository**: [ChatNova Project](https://github.com/PavanKhamitkar/ChatNova)
- **Live Demo**: [Try ChatNova](https://chatnova-0ldf.onrender.com)
