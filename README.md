# Twitter Bot with GPT Integration

A sophisticated Twitter bot that automatically engages with mentions and timeline tweets using OpenAI's GPT model for generating human-like responses.

## Features

- Automated responses to mentions
- Timeline scanning and engagement
- GPT-powered response generation
- Rate limiting protection
- Scheduled operations

## Prerequisites

- Python 3.6+
- Twitter Developer Account with API credentials
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd twitter-bot
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your credentials:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the bot using:
```
bash
python twitter_bot.py
```

The bot will:
- Check for new mentions every 15 minutes
- Scan the timeline every 30 minutes
- Automatically generate and post responses using GPT-4

## Configuration

The bot's behavior can be customized by modifying:
- Response generation parameters (temperature, max tokens)
- Engagement logic in the `should_engage` method
- Scheduling intervals
- Rate limiting delays

## Dependencies

The project relies on the following main packages:
- tweepy (Twitter API client)
- openai (OpenAI API client)
- python-dotenv (Environment variable management)
- schedule (Task scheduling)

## Error Handling

The bot includes comprehensive error handling for:
- API rate limits
- Network issues
- Authentication errors
- Response generation failures

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Add your chosen license here]

## Disclaimer

Please ensure compliance with Twitter's API terms of service and usage guidelines when deploying this bot.