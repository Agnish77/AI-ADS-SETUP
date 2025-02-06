# AI Chatbot for Google Ads Automation

## Overview

This project is a full-stack AI-powered chatbot that interacts with business owners to understand their niche and automates the creation of Google Ads campaigns. The chatbot uses **DeepSeek AI** for text generation and integrates with the **Google Ads API** to generate and pre-fill campaign details.

## Features

- AI-powered chatbot to collect business details
- Automated Google Ads campaign creation
- Full-stack application with **React.js (Frontend)** and **FastAPI (Backend)**
- Secure API calls to Google Ads
- Ad preview screen before campaign launch

## Tech Stack

- **Frontend:** React.js
- **Backend:** FastAPI (Python)
- **AI Model:** DeepSeek AI (Hugging Face)
- **Database:** PostgreSQL / Firebase (Optional for storing data)
- **Google Ads API:** For campaign automation

## Installation & Setup

### 1️⃣ Clone the Repository


git clone https://github.com/Agnish77/AI-ADS-SETUP
cd ai-ads-chatbot


### 2️⃣ Backend Setup (FastAPI)


cd backend
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate    # For Windows
pip install -r requirements.txt
uvicorn main:app --reload


### 3️⃣ Frontend Setup (React.js)


cd frontend
npm install
npm start


## Usage

1. Open the frontend at `http://localhost:3000`
2. Interact with the chatbot to enter business details
3. Review the AI-generated ad campaign preview
4. Click **Launch Ad** to submit the campaign via Google Ads API

## Environment Variables

Create a `.env` file in the **backend** directory with:


HUGGINGFACE_API_KEY=your_huggingface_token

GOOGLE_ADS_CLIENT_ID=your_client_id

GOOGLE_ADS_CLIENT_SECRET=your_client_secret

GOOGLE_ADS_DEVELOPER_TOKEN=your_developer_token


## Troubleshooting

- **npx not found?** Run `npm install -g create-react-app`
- **Google Ads API errors?** Ensure API keys and OAuth credentials are correct.
- **Model download failing?** Try downloading manually from Hugging Face and load it locally.

## Future Improvements

- Improve AI-generated ad content quality
- Add support for multiple ad formats (Search, Display, Video)
- Implement analytics for campaign performance tracking



## Author

Developed by **Agnish Paul**

---

###
