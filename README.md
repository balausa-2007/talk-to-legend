⚔️ Talk to a Legend
Speak with the great figures of Kazakh history
 

Concept:
The user selects a historical figure from Kazakhstan and starts a conversation with them. The AI responds in the first person, fully adopting the style, tone, mannerisms, and personality of that person.

About the Project
Talk to a Legend is an AI-powered web application that allows users to have real conversations with legendary historical figures of Kazakhstan. Powered by RAG (Retrieval-Augmented Generation) and Groq LLaMA, each character responds in their own unique voice — in Kazakh, Russian, or English.


How It Works
User Question
     ↓
ChromaDB searches relevant knowledge chunks
     ↓
Context + Persona Prompt → Groq LLaMA API
     ↓
Character responds in user's language


Historical Characters
Character	Period	Known For
⚔️ Tomiris	6th century BC	Queen of Massagetae, defeated Cyrus the Great
📜 Abai Kunanbayev	1845–1904	Poet, philosopher, enlightener
🏇 Kenesary Kassymov	1802–1847	Last Khan of the Kazakhs, national hero
🎖️ Bauyrjan Momyshuly	1910–1982	Hero of WWII, defender of Moscow
 



Sample Questions to Ask
⚔️ Tomiris (English)
•	"How did you feel when your son Spargapis was captured by Cyrus?"
•	"What tactics did you use to defeat the Persian army?"
•	"What does it mean to be a queen in a world of male rulers?"
•	"Would you negotiate peace with Cyrus if you could go back?"
•	"What is your greatest lesson for modern leaders?"
📜 Абай Кунанбаев (Русский)
•	"Что ты думаешь о невежестве казахского народа?"
•	"Какое твоё любимое произведение Пушкина и почему?"
•	"Что означают для тебя «Слова назидания»?"
•	"Как ты относился к русской культуре?"
•	"Что бы ты сказал молодёжи сегодня?"
•	“Сколько у вас детей”
🏇 Кенесары Касымов (Русский)
•	"Почему ты не принял условия мира с Россией?"
•	"Что ты чувствовал, зная что можешь проиграть?"
•	"Как ты относился к своим воинам?"
•	"Чем ты гордишься больше всего?"
•	"Что значит быть последним ханом казахов?"
•	“вы ненавидите кыргызов?”
🎖️ Бауыржан Момышұлы (Қазақша)
•	"Мәскеуді қорғаған кезде не сезіндіңіз?"
•	"Панфилов генералы сізге не үйретті?"
•	"Соғыста ең қиын сәт қандай болды?"
•	"Қазақ халқына не айтар едіңіз?"
•	"Батыр деген кім?"



Tech Stack
Layer	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python, FastAPI
AI Model	LLaMA 3.3 70B via Groq API
RAG	LangChain + ChromaDB
Embeddings	paraphrase-multilingual-MiniLM-L12-v2
Languages	Kazakh 🇰🇿 / Russian / English


Project Structure
talk-to-legend/
├── data/
│   ├── abai.txt
│   ├── bauyrjan.txt
│   ├── kenesary.txt
│   └── tomiris.txt
├── backend/
│   ├── main.py        # FastAPI server
│   ├── rag.py         # RAG pipeline
│   └── personas.py    # Character prompts
├── frontend/
│   └── index.html     # Web interface
├── .env               # API keys
└── README.md


Features
•	🌐 Multilingual — chat in Kazakh, Russian, or English
•	🧠 RAG-powered — characters answer based on real historical knowledge
•	🎭 Persona prompting — each character has a unique voice and personality
•	⚡ Fast responses — powered by Groq's ultra-fast inference
•	📱 Clean UI — elegant dark theme inspired by ancient history


Author
Balausa Nurdaulet 250107085
SDU University — CSS 118: AI & Prompt Engineering
2025 year


"To become a human being, one must learn." — Abai Kunanbayev

