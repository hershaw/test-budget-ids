# Budget Posting Script

This Python script posts budget data to a specified API endpoint using OAuth authentication.

## Requirements

- Python 3.9 or later
- No external libraries (uses only Python standard library)

## Environment Variables

You must set the following environment variables before running the script:

- `OAUTH_CLIENT_ID`: Your OAuth client ID
- `OAUTH_CLIENT_TOKEN`: Your OAuth client secret/token
- `API_ENDPOINT`: The API endpoint where the payload will be posted (e.g., `https://api.example.com/budget`)

## Usage

1. Set the required environment variables:

   **Linux / macOS:**

   ```bash
   export OAUTH_CLIENT_ID="your_client_id"
   export OAUTH_CLIENT_TOKEN="your_client_token"
   export API_ENDPOINT="https://api.example.com/budget"
   ```

   **Windows:**

   ```bash
    setx OAUTH_CLIENT_ID "your_client_id"
    setx OAUTH_CLIENT_TOKEN "your_client_token"
    setx API_ENDPOINT "https://api.example.com/budget"
   ```

```

python budget_post.py

```
