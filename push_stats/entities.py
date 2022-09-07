from dataclasses import dataclass

@dataclass
class Arguments:
    input_stats_dir: str
    checkpoint_dir: str

@dataclass
class APILoadResponse:
    payload: str
    status_code: int
    response_content: str
