#GitTreats

GitTreats is a system which rewards developers for committing code to GitHub by dispensing a treat.

## Requirements
To get started with GitTreats you'll need a few things

- A [GitHub](https://github.com/) account
- A [Pubnub](https://www.pubnub.com/) Account and Keyset
- A computer (with FQDN) to act as a server
- A Raspberry Pi to act as the client

## Installation

### Server

On the server clone this repository

`git clone https://github.com/sedders123/GitTreats`

Then set up your PubNub Keys to be environment variables

`export PUBNUB_GT_PUBLISH={Your Publish Key Here}`

`export PUBNUB_GT_SUBSCRIBE={Your Subscribe Key Here}`

Next install the python packages

`pip install -r requirements.txt`

Modify the `USER_NAME` variable in the [server.py](server.py) file, to be your GitHub username

In the repositories that you wish to be rewarded for go to the setting tab and add a Webhook that points to your server.

Under 'Which events would you like to trigger this webhook?' choose 'Let me select individual events' and then tick 'Pull request' only

## Usage

On the server simply run `python server.py`
