from activitysim.benchmarking.componentwise import (
    template_component_timings,
    template_setup_cache,
)

from .sandag_example import *

EXAMPLE_NAME = "example_sandag_2_zone"
CONFIGS_DIRS = ("configs_2_zone", "example_psrc/configs")
DATA_DIR = "data_2"
OUTPUT_DIR = "output_2"
VERSION = "1"


def setup_cache():
    template_setup_cache(
        EXAMPLE_NAME,
        COMPONENT_NAMES,
        BENCHMARK_SETTINGS,
        dict(
            read_skim_cache=SKIM_CACHE,
            write_skim_cache=SKIM_CACHE,
        ),
        CONFIGS_DIRS,
        DATA_DIR,
        OUTPUT_DIR,
    )


template_component_timings(
    globals(),
    COMPONENT_NAMES,
    EXAMPLE_NAME,
    CONFIGS_DIRS,
    DATA_DIR,
    OUTPUT_DIR,
    PRELOAD_INJECTABLES,
    REPEAT,
    NUMBER,
    TIMEOUT,
    VERSION,
)
