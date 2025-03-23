# ReelReplyAI 

## Overview  
ReelReplyAI is an automated Instagram direct message reply bot designed to respond to reel messages. It analyzes top comments from a reel and generates appropriate replies using AI. The bot runs continuously, ensuring timely and context-aware responses.  

## Features  
- **Automated Responses**: Detects and replies to new reel messages automatically.  
- **AI-Generated Replies**: Uses AI to craft relevant and engaging responses.  
- **Instagram Direct Message Integration**: Works with Instagram’s direct messaging system.  
- **Comment Analysis**: Extracts top comments from reels to provide context-aware replies.  
- **Efficient and Secure**: Uses API authentication and avoids redundant replies.  

## Technology Used  
- **Programming Language**: Python  
- **Libraries/Frameworks**:  
  - `instagrapi` – For Instagram API integration  
  - `google.generativeai` – For AI-generated responses  
  - `apify-client` – For extracting reel comments  
  - `dotenv` – For managing environment variables  
  - `json` – For tracking replied messages  
  - `os`, `time` – For handling file operations and scheduling  

## Installation  

1. Clone the repository:  
   ```sh
   git clone https://github.com/shourypandya/ReelReplyAI.git
   ```  
2. Navigate to the project directory:  
   ```sh
   cd ReelReplyAI
   ```  
3. Install dependencies:  
   ```sh
   pip install instagrapi google-generativeai apify-client python-dotenv
   ```  
4. Set up environment variables:  
   - Rename the file name .env.example to .env only
   - Create a `.env` file in the project root.  
   - Add your credentials:  
     ```
     GOOGLE_API_KEY=your_gemini_api_key
     APIFY_KEY=your_apify_key
     INSTA_USERNAME=your_instagram_username
     INSTA_PASSWORD=your_instagram_password
     ```  
5. Run the script:  
   ```sh
   python reelreply.py
   ```  

## Usage  

### How It Works  
- The bot checks for new reel messages every 10 seconds.  
- It retrieves the top three comments from the reel.  
- AI generates a response based on these comments.  
- The reply is sent automatically to the sender.  

### Notes  
- The bot ensures no duplicate replies by maintaining a record of responded messages.  
- If the AI response starts with unnecessary quotation marks, it removes them before sending.  

## Contributing  
If you want to contribute to this project, fork the repository, make necessary improvements, and submit a pull request. Ensure that your changes follow best practices and are well-documented.  

## License  
This project is open source and available under the MIT License.  

## Contact  
- **Name**: Shoury Pandya  
- **B.Tech 3rd Year**  
- **Stream**: Artificial Intelligence and Data Science  
- **College**: AD Patel Institute Of Technology, CVM University  
- **GitHub Profile**: [Your GitHub](https://github.com/ShouryPandya)  
- **LinkedIn Profile**: [Your LinkedIn](https://linkedin.com/in/shourypandya)  
