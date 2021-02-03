
# -*- coding: utf-8 -*-

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import List, NoReturn

from .utils import UUIDEncoder


class AggregateRoot(ABC):
    """
    Aggregate Root
    """

    def as_str(self):
        """
        Entity as str
        """
        _dict = asdict(self)
        parsed_dict = json.dumps(_dict, cls=UUIDEncoder)
        return parsed_dict

    def as_dict(self):
        """
        Entity as dict
        """
        parsed_dict = json.loads(self.as_str())
        return parsed_dict

    def __repr__(self):
        return self.as_dict()

