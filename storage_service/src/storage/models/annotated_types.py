from typing import Annotated

from sqlalchemy import types, func
from sqlalchemy.orm import mapped_column

from datetime import datetime

str_256 = Annotated[str, mapped_column(types.String(256))]
pk = Annotated[int, mapped_column(types.BIGINT, primary_key=True)]
timestamp = Annotated[datetime, mapped_column(server_default=func.current_timestamp())]