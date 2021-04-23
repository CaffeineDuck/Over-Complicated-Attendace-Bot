# Attendance Bot

## About Me
This is a bot to do your online class attendance. But its not just that. It is a code where I overcomplicate the things without any real work or meaning. It doesn't cover any edge cases. But I made the code long just for the fun of it, when the whole code code have been completed in 100 lines or less.

## How it works?
After you start the script, after some pre-checks it starts taking the attendance. The start_time you specified won't make any difference in the attendance except for the initial-check. Which means, if you start the script at 9:14 AM and have interval of 3600 seconds (1 Hour) then the bot will take the next attendance at 10:14 AM regardless of start_time and end_time unless either start_time or end_time are greater or lower than 10:14 AM.

## Requirements
1. Python 3.9 or greater
2. Pipenv
3. Chrome

## How to use?
1. Clone the repo in your local machine.
2. Run `pipenv install`.
3. Download chromedriver.
4. Create a file named `.env` and populate files using the format provided in [.env](example-dot-env.txt).
5. Run `python -m bot`.

## How to contribute?
1. Fork the repo.
2. Added features/ solve bugs.
3. Create a pull request.
4. Wait for my response.
