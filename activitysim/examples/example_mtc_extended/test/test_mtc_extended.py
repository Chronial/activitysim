# ActivitySim
# See full license in LICENSE.txt.
import os
import subprocess
import pkg_resources

import pandas as pd
import pandas.testing as pdt

from activitysim.core import inject


def teardown_function(func):
    inject.clear_cache()
    inject.reinject_decorated_tables()


def test_mtc_extended():

    def example_path(dirname):
        resource = os.path.join('examples', 'example_mtc_extended', dirname)
        return pkg_resources.resource_filename('activitysim', resource)

    def example_mtc_path(dirname):
        resource = os.path.join('examples', 'example_mtc', dirname)
        return pkg_resources.resource_filename('activitysim', resource)

    def test_path(dirname):
        return os.path.join(os.path.dirname(__file__), dirname)

    def regress():
        regress_trips_df = pd.read_csv(test_path('regress/final_trips.csv'))
        final_trips_df = pd.read_csv(test_path('output/final_trips.csv'))

        regress_vehicles_df = pd.read_csv(test_path('regress/final_vehicles.csv'))
        final_vehicles_df = pd.read_csv(test_path('output/final_vehicles.csv'))

        # person_id,household_id,tour_id,primary_purpose,trip_num,outbound,trip_count,purpose,
        # destination,origin,destination_logsum,depart,trip_mode,mode_choice_logsum
        # compare_cols = []
        pdt.assert_frame_equal(final_trips_df, regress_trips_df)
        pdt.assert_frame_equal(final_vehicles_df, regress_vehicles_df)

    file_path = os.path.join(os.path.dirname(__file__), 'simulation.py')

    subprocess.run(['coverage', 'run', '-a', file_path,
                    '-c', test_path('configs'), '-c', example_path('configs'),
                    '-c', example_mtc_path('configs'),
                    '-d', example_mtc_path('data'),
                    '-o', test_path('output')], check=True)

    regress()


if __name__ == '__main__':

    test_mtc_extended()
