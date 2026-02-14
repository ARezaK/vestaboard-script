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
LOCAL_IP_ADDRESS = '192.168.1.28'
LOCAL_API_TOKEN = os.environ['LOCAL_API_TOKEN']
KANYE_API_URL = 'https://api.kanye.rest'

# limit is 124 characters for quote and person
QUOTES = [
    ('Show yourself some respect and stop doing stupid shit that makes you age faster and feel miserable.', 'Bryan Johnson'),
    ("It is not necessary to accept the choices handed down to you by life as you know it. There is more to it than that", 'HST'),
    ("Invest First, Investigate Later", 'George Soros (on equity investing)'),
    ("Whats something youve learned that you believe gives you an edge?", 'Unknown'),
    ("Your worst sin is that you have destroyed and betrayed yourself for nothing", "Dostoyevksy"),
    ("you're a healer main because you want to help people, i'm a healer main because i'm spiteful and don't trust anyone else. we are not the same", 'sariel (twitter)'),
    ("When you choose the benefits of an action, you also choose the drawbacks.", 'Unknown'),
    ("Your willingness to believe something is influenced by how much you want and need it to be true.", 'Unknown'),
    ('To enjoy bodily warmth, some small part of you must be cold, for there is no quality in this world that is not what it is merely by contrast.', "Moby Dick"),
    ("You're the total of the 5 people you hang out with. Often I don't hang out with good people or even 5 people. Reading fills that gap.", "Unknown"),
    ("Someone with half your IQ is making 10x as you because they aren't smart enough to doubt themselves.", 'Ed Latimore'),
    ("Solitude is dangerous. It's very addictive. It becomes a habit after you realize how calm and peaceful it is.", "Jim Carrey"),
    ("Man can not remake himself without suffering for he is both the marble and the sculptor", "Unknown"),
    ("If a decision is reversible, biggest risk is moving too slow. If a decision is irreversible, biggest risk is moving too fast", "Unknown"),
    ("The older I get the more I realize how many kinds of smart there are. There are lots of kinds of stupid, too", "J. Bezos"),
    ("The teacher learns more than the student. The author learns more than the reader.The speaker learns more than that attending. The way to learn is by doing", "Unknown"),
    ("Invest in preparedness, not in prediction", 'Nassim Taleb'),
    ("First step of any meaningful pursuit is to severely underestimate its difficulty", 'Sara Hooker'),
    ("How can you create an enviroment that will naturally bring about my desired change?", "Unknown"),
    ("Your life is purchased by where you spend attention ", "Unknown"),
    ("If you don't make time for your wellness you will be forced to make time for your illness", "Unknown"),
    ("Being good in business is the most fascinating kind of art.", "Andy Warhol"),
    ("The only real test of intelligence is if you get what you want out of life", "Naval"),
    ("Habits are the compound interest of self-improvement. A small habit when repeated consistently grows into something significant.", "Unknown"),
    ("Six Most Important Luxuries in life: Time, Health, A Quiet Mind, Slow Mornings, Meaningful Work, A House Full of Love", "Unknown"),
    ("You sensed that you should be following a different path, a more ambitious one, that you were destined for other things but you had no idea how to achieve them and in your misery you began to hate everything around you", "Unknown"),
    ("No Risk, No Rari", "Unknown"),
    ("You run into an asshole in the morning, you've ran into an asshole. You run into assholes all day, you're the asshole.", "Unknown"),
    ("You never know what worse luck your bad luck saved you from", "Cormac McCarthy"),
    ("Take Yourself Seriously - The way the world treats you can be a reflection of how you treat yourself", "Unknown"),
    ("Better to admit you walked through the wrong door then spend your life in the wrong room", "Unknown"),
    ("There is an inverse relationship between something on your mind and how much its getting done", "David Allen"),
    ("If you are distressed by anything external, the pain is only due to your estimate of it", "M. Aurelius"),
    ("I can no longer obey; I have tasted command, and I cannot give it up.", "N. Bonaparte"),
    ("The greater the artist, the greater the doubt; perfect confidence is granted to the less talented as a consolation price", "R. Hughes"),
    ("A little learning is a dangerous thing. Drink deep or taste not the Pierian spring", "A. Pope"),
    ("Life is but a search for a permanent witness", "Unknown"),
    ("The more disciplined your environment is, the less disciplined you need to be. Don't swim upstreamh", "Unknown"),
    ("Doubt is not an agreeable condition, but certainty is an absurd one", "Voltaire"),
    ("4 most expensive words in American history: This time its different", "Sir John Templeton"),
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
        else:
            print(f"quote is too long: {quote}")

# Main execution logic
quote = get_valid_quote()

local_board = Board(localApi={'ip': LOCAL_IP_ADDRESS, 'key': LOCAL_API_TOKEN})
local_board.post(f"{quote[0]}\n- {quote[1]}")
