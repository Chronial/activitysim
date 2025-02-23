import sys
import os


def main():

    # set all these before we import numpy or any other math library
    if len(sys.argv) > 1 and sys.argv[1] == "benchmark":
        os.environ['MKL_NUM_THREADS'] = '1'
        os.environ['OMP_NUM_THREADS'] = '1'
        os.environ['OPENBLAS_NUM_THREADS'] = '1'
        os.environ['NUMBA_NUM_THREADS'] = '1'
        os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
        os.environ['NUMEXPR_NUM_THREADS'] = '1'

    from activitysim.cli import CLI
    from activitysim.cli import run
    from activitysim.cli import create
    from activitysim.cli import benchmark

    from activitysim import __version__, __doc__

    asim = CLI(version=__version__,
               description=__doc__)
    asim.add_subcommand(name='run',
                        args_func=run.add_run_args,
                        exec_func=run.run,
                        description=run.run.__doc__)
    asim.add_subcommand(name='create',
                        args_func=create.add_create_args,
                        exec_func=create.create,
                        description=create.create.__doc__)
    asim.add_subcommand(name='benchmark',
                        args_func=benchmark.make_asv_argparser,
                        exec_func=benchmark.benchmark,
                        description=benchmark.benchmark.__doc__)
    sys.exit(asim.execute())
