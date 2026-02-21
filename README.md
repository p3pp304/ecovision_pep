♻️ **EcoVision: Smart Waste Sorting Assistant**
EcoVision is a smart web application designed to optimize domestic waste sorting. By leveraging a hybrid approach that combines Multimodal LLMs and Geolocation, the system accurately identifies waste and provides disposal instructions based on the specific regulations of the user's municipality.

🌐 **Live Demo**
You can test the application live at the following address:
👉 https://ecovision-g3.streamlit.app/

Note: The live demo is powered by a dedicated API quota. Should the application fail to respond, the daily request limit may have been reached.

🌟 Key Features
-Multimodal Recognition: Advanced visual analysis powered by Google Gemini 2.5 Flash to identify materials and the current state of the waste.
-Complex Object Decomposition: Capability to distinguish and separate components of multi-material waste (e.g. a bottle and its cap), providing distinct disposal routes for each part.
-Dynamic Geolocation: Real-time adaptation of disposal rules based on the user's GPS position via Reverse Geocoding.
-Integrated Chatbot: A conversational assistant with context memory to resolve specific post-analysis queries.
-Recycling Center Maps: Google Maps integration to locate local collection centers for special or hazardous waste.

🐳 **Docker Installation Guide**
Utilizing Docker containers ensures maximum environment consistency across development and production stages.

🛠 **Hardware and Software Prerequisites**
-Virtualization: Must be enabled in the PC BIOS (Intel VT-x or AMD-V) for Docker Desktop to function.
-Docker Desktop: Installed and currently in a "running" state.
-Municipal Database: Ensure the comuniitaliani.json file is present in the project's root directory.

🔑 **API Key Management (Security)**
For security purposes, API keys are never uploaded to Git. The system is configured to read the key from environment variables or Streamlit Secrets, ensuring that sensitive credentials remain unexposed within the source code.

🚀 **Startup Commands**
Build the Image:
Open the terminal in the project root and create the Docker image:

Bash
docker build -t ecovision-app .
Run the Container:
Launch the application by passing your personal key via the -e environment variable:

Bash
docker run -p 8501:8501 -e GOOGLE_API_KEY="INSERT_YOUR_KEY_HERE" ecovision-app
-p 8501:8501: Maps the container's port to your local machine's port.

-e GOOGLE_API_KEY: Securely injects the API key into the system.

🌐 **Accessing the App**
Once the container is running, the app can be accessed via your browser at:
👉 http://localhost:8501
(Note: Disregard the 0.0.0.0 address shown in the terminal, as it is an internal container reference).

📂 **Project Structure and Diagrams**
Detailed technical documentation can be found within the repository folders:

Use Case Diagram: Includes the "Ask the Expert" Chatbot and API Key management workflows.

Class Diagram: Reflects the multi-component architecture of the AI analysis and JSON parsing.

Sequence Diagram: Illustrates the asynchronous flow toward the google-genai SDK.

👥 **Authors**
Alessio Cappiello, Andrea Falcicchio, Giuseppe Fuzio

Project developed for the Software Engineering course - Polytechnic of Bari (A.Y. 2025/26).

