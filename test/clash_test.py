import lulu

# from dotenv import load_dotenv
# import os


# load_dotenv()
# key = os.getenv("KEY")


def test_by_puuid():
    clash_data = lulu.clash.clash()

    assert clash_data == "This is some clash data"
