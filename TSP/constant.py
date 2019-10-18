from enum import Enum

class INPUT_TYPE(Enum):
    JSON = '.json'
    CSV = '.csv'

INPUT = INPUT_TYPE.CSV

class EDGE_TPYE(Enum):
    DEPOSITION = 0
    ROTATION = 1
    IDLE = 2

DEPOSITION_COST = 5