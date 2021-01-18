import os
from typing import Literal

STAGE: Literal["production", "dev", "debug"] = os.environ.get("STAGE", "debug")
