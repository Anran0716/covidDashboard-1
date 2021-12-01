from pipeline_tools import run_transform_gbq
from pathlib import Path

sql_dir = Path(__file__).parent / 'sql'

def main():
    run_transform_gbq('staging', 'test_hosp_death', sql_dir)
    run_transform_gbq('staging', 'wk_case_death', sql_dir)
    run_transform_gbq('staging', 'NYC_map', sql_dir)
    run_transform_gbq('staging', 'vac_now_neigh', sql_dir)
    run_transform_gbq('final', 'covid_map', sql_dir)


if __name__ == '__main__':
    main()