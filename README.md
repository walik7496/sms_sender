# sms_sender

A simple Python script to send SMS messages via the Sinch API.

## Installation

1. Install Python 3.x: [Download Python](https://www.python.org/downloads/).
2. Install the required Python libraries:

```bash
pip install requests
```

# Usage

1. Ensure you have a valid `access_token.txt` file with your API access token.
2. Set the `service_plan_id`, `from_`, and `to_` variables with appropriate values. 
   - `service_plan_id`: Your unique service plan ID.
   - `from_`: The sender's phone number.
   - `to_`: The recipient's phone number.
3. Run the Python script to send an SMS message using the Sinch API.

# Code Explanation

- **Get Access Token**: Reads the API access token from `access_token.txt`.
- **Headers**: Sets the authorization header with the access token and specifies the content type as JSON.
- **Payload**: Contains the SMS message details, including the `from_` number, `to_` list, and the message body (`'Hello, Dear'`).
- **Sending SMS**: The `r.post()` method sends the SMS request to the Sinch API endpoint with the payload and headers.

# Troubleshooting

- **Invalid Access Token**: Ensure your `access_token.txt` file contains a valid token.
- **Incorrect Phone Numbers**: Verify that the `from_` and `to_` phone numbers are correctly formatted.
- **API Limitations**: Ensure that the Sinch API allows sending SMS to the specified phone numbers based on your service plan.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact

If you have any questions or need further assistance, feel free to open an issue or reach out directly to the repository owner.
