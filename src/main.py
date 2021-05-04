import os
from typing import Optional
from bot import run

# Main entrypoint
def main():

    bot_token: Optional[str] = None

    try:
        bot_token = os.environ['BOT_TOKEN']
    except KeyError:
        print('The environment variable BOT_TOKEN is not defined')
        exit(1)

    run(bot_token)


if __name__ == "__main__":
    main()