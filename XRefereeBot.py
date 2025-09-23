import argparse
from src.handlers import handle_mention_event
from src.twitter_client import poll_mentions_loop
from src.judge import test_local

def main():
    parser = argparse.ArgumentParser(description="Debate Ref Bot")
    parser.add_argument("--test", action="store_true", help="Run a local test")
    parser.add_argument("--poll", action="store_true", help="Poll Twitter mentions")
    args = parser.parse_args()

    if args.test:
        test_local()
    elif args.poll:
        poll_mentions_loop()
    else:
        print("Usage: python debate_ref_bot.py --test | --poll")

if __name__ == "__main__":
    main()
