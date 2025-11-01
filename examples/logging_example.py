import logging

from pyke import Pyke

# Configure logging before creating Pyke instance
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

api = Pyke("RGAPI-...")
