# fun_spammer_simulator.py

import time
import random
from config import api_id, api_hash, phone_number, target_group

fun_facts = [
    "The $FUN token is a revolutionary asset in crypto gaming.",
    "With $FUN, you can explore decentralized betting and casinos.",
    "The power of $FUN lies in its smart contract capabilities.",
    "$FUN is fast, cheap, and perfect for micro-transactions.",
    "Did you know $FUN is accepted on multiple gaming platforms?",
    "HODL $FUN for the future of Web3 entertainment.",
    "$FUN is designed for fast, secure, and anonymous gaming.",
    "Use $FUN to play, earn, and grow your digital wealth.",
    "$FUN provides liquidity in many DeFi ecosystems.",
    "$FUN isn't just a token, it's a movement in gaming."
]

def generate_fun_message():
    selected = random.sample(fun_facts, k=4)
    message = ' '.join(selected)
    while message.count("$FUN") < 5 or len(message.split()) < 30:
        extra = random.choice(fun_facts)
        message += ' ' + extra
    return message

def send_message(group_id, message):
    # Simulated print instead of real API call
    print(f"[Sending to {group_id}]")
    print(message)
    print("-" * 80)

def main():
    sent_messages = set()

    while True:
        message = generate_fun_message()

        # Ensure message is unique
        while message in sent_messages:
            message = generate_fun_message()

        sent_messages.add(message)

        send_message(target_group, message)

        sleep_time = random.randint(120, 180)
        print(f"Sleeping for {sleep_time} seconds...\n")
        time.sleep(sleep_time)

if __name__ == "__main__":
    print(f"Using API ID: {api_id}, Hash: {api_hash}")
    print(f"Simulating login for phone: {phone_number}")
    main()
