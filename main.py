"""
from vestaboard import Board
localBoard = Board(localApi={ 'ip': '192.168.1.12', 'enablementToken': '*****' })
Success! Here's your local API token:
ABCDEF
Saved to ./local.txt! This instance of Board can now be used with the local API, or pass the `localApi={'useSavedToken': True}` when instantiating a new Board to use your saved credentials.
localBoard2 = Board(localApi={'ip': '192.168.1.12', 'key': 'ABCDEF'})
currentmessage = localBoard2.read()
localBoard2.read({'print': True})
{'message': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [13, 18, 0, 19, 21, 19, 8, 0, 19, 1, 25, 19, 0, 8, 5, 0, 8, 15, 16, 5, 19, 0], [20, 15, 0, 8, 1, 22, 5, 0, 20, 8, 5, 0, 2, 2, 8, 0, 7, 9, 22, 5, 0, 0], [13, 15, 18, 5, 0, 19, 12, 15, 16, 16, 25, 0, 6, 15, 15, 20, 0, 0, 0, 0, 0, 0], [13, 1, 19, 19, 1, 7, 5, 19, 0, 20, 15, 0, 13, 18, 0, 13, 25, 0, 7, 21, 25, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}
{'message': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [13, 18, 0, 19, 21, 19, 8, 0, 19, 1, 25, 19, 0, 8, 5, 0, 8, 15, 16, 5, 19, 0], [20, 15, 0, 8, 1, 22, 5, 0, 20, 8, 5, 0, 2, 2, 8, 0, 7, 9, 22, 5, 0, 0], [13, 15, 18, 5, 0, 19, 12, 15, 16, 16, 25, 0, 6, 15, 15, 20, 0, 0, 0, 0, 0, 0], [13, 1, 19, 19, 1, 7, 5, 19, 0, 20, 15, 0, 13, 18, 0, 13, 25, 0, 7, 21, 25, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}
localBoard2.post("Helllo")
"""
from typing import Tuple
from vestaboard import Board
import argparse
import requests
import random
import os

# Constants for API setup
LOCAL_IP_ADDRESS = '192.168.1.12'
LOCAL_API_TOKEN = os.environ['LOCAL_API_TOKEN']
KANYE_API_URL = 'https://api.kanye.rest'

# limit is 124 characters for quote and person
QUOTES = [
    ('Show yourself some respect and stop doing stupid shit that makes you age faster and feel miserable.', 'Bryan Johnson'),
    ("It is not necessary to accept the choices handed down to you by life as you know it. There is more to it than that", 'HST'),
    ("Invest First, Investigate Later", 'George Soros (on equity investing'),
    ("Whats something youve learned that you believe gives you an edge", 'Unknown'),
    ("Your worst sin is that you have destroyed and betrayed yourself for nothing", "Dostoyevksy"),
    ("you're a healer main because you want to help people, i'm a healer main because i'm spiteful and don't trust anyone else to do it properly. we are not the same", 'sariel (twitter)'),
    ("When you choose the benefits of an action, you also choose the drawbacks.", 'Unknown'),
    ("Your willingness to believe something is influenced by how much you want and need it to be true.", 'Unknown'),
    ('To enjoy bodily warmth, some small part of you must be cold, for there is no quality in this world that is not what it is merely by contrast. Nothing exists in itself.', "Moby Dick"),
    ("I believe in the idea that you are the sum total of the 5 people you hang out with. Sotimetimes I don't hang out with good people or even 5 people. Reading is a way of filling that gap.", "Unknown"),
    ("Someone with half your IQ is making 10x as you because they aren't smart enough to doubt themselves.", 'Ed Latimore (Twitter)'),
    ("Solitude is dangerous. It’s very addictive. It becomes a habit after you realize how calm and peaceful it is.", "Jim Carrey"),
    ("Man can not remake himself without suffering for he is both the marble and the sculptor", "Unknown"),
    ("If a decision is reversible, the biggest risk is moving too slow. " + '\n' + " If a decision is irreversible, the biggest risk is moving too fast", "Unknown"),
    ("The teacher learns more than the student " + "\n" + "The author learns more than the reader" + "\n" + "The speaker learns more than that attending" + "\n" + "The way to learn is by doing", "Unknown"),
    ("Invest in preparedness, not in prediction", 'Nassim Taleb'),
    ("How can you create an enviroment that will naturally bring about my desired change?", "Unknown"),
    ("Your life is purchased by where you spend attention ", "Unknown"),
    ("Being good in business is the most fascinating kind of art. Making money is art and working is art and good business is the best art.", "Andy Warhol"),
]


# check to see if any argument passed to the script
parser = argparse.ArgumentParser(
                    prog='VestaBoard Management',
                    description='Control your vestaboard',
                    epilog='FBGM')

parser.add_argument('-k', '--kanye', action='store_true', help="Use a Kanye quote")
parser.add_argument('-o', '--own', action='store_true', help="Use an own quote")
args = parser.parse_args()


def get_kanye_quote() -> Tuple[str, str]:
    response = requests.get(KANYE_API_URL)
    response.raise_for_status()  # Ensure we handle failed requests
    quote = response.json()['quote']
    return quote, 'Kanye'


# Fetch random own quote
def get_random_own_quote() -> Tuple[str, str]:
    return random.choice(QUOTES)


# Select the quote based on arguments or randomness
def get_selected_quote() -> Tuple[str, str]:
    if args.kanye:
        return get_kanye_quote()
    elif args.own:
        return get_random_own_quote()
    return get_kanye_quote() if random.random() > 0.5 else get_random_own_quote()


def get_valid_quote() -> Tuple[str, str]:
    """Get a valid quote that fits within the character limit."""
    while True:
        quote = get_selected_quote()
        # Check if the quote is too long
        print(f"Got Quote: {quote}")
        if len(quote[0]) + len(quote[1]) <= 124:
            return quote  # Return the valid quote if it fits the limit

# Main execution logic
quote = get_valid_quote()

local_board = Board(localApi={'ip': LOCAL_IP_ADDRESS, 'key': LOCAL_API_TOKEN})
local_board.post(f"{quote[0]}\n- {quote[1]}")
