import sys
from push_stats.entities import Arguments


def parse_arguments() -> Arguments:
    if len(sys.argv) != 3:
        sys.exit(1)

    return Arguments(
        input_stats_dir=sys.argv[1],
        checkpoint_dir=sys.argv[2],
    )
