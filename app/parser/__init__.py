from typing import Dict, IO, Generator
from app.models import Run, Relic
import json


class RunParser:
    def parse_from_file(self, file: IO):
        data = json.load(file)
        return self.parse_from_dict(data)

    def parse_from_dict(self, data: Dict) -> Run:
        run = Run()

        return run


class RelicParser:
    def parse_from_file(self, file: IO):
        data = json.load(file)
        return self.parse_from_dict(data)

    def parse_from_dict(self, dict: Dict) -> Generator[Relic, None, None]:
        for name, data in dict.items():
            if "Test" in name:
                continue
            yield Relic(name=name, flavor=data['FLAVOR'])
