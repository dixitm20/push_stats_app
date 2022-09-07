import json
import os

from push_stats.arguments import parse_arguments
from push_stats.extract import get_stats_files, get_success_brand_list, get_input_stats
from push_stats.load import load_to_api


def main() -> None:
    arguments = parse_arguments()
    input_stats_dir_name = os.path.basename(os.path.normpath(arguments.input_stats_dir))
    checkpoint_complete_path = os.path.join(arguments.checkpoint_dir, input_stats_dir_name)

    if not os.path.exists(checkpoint_complete_path):
        os.makedirs(checkpoint_complete_path)

    for stats_file in get_stats_files(arguments.input_stats_dir):
        print(f"Processing stats file: {stats_file}")
        stats_file_complete_path = os.path.join(arguments.input_stats_dir, stats_file)
        checkpoint_file_complete_path = os.path.join(checkpoint_complete_path, f"success-{stats_file}")

        success_brands_list = get_success_brand_list(checkpoint_file_complete_path)
        current_file_success_stats_list = []
        current_file_failed_stats_list = []
        current_file_skipped_stats_list = []

        for stats in get_input_stats(stats_file_complete_path):
            if stats['brand'] not in success_brands_list:
                api_response = load_to_api(stats)
                if api_response.status_code == 200:
                    current_file_success_stats_list.append(api_response.payload)
                else:
                    current_file_failed_stats_list.append(api_response.payload)
            else:
                current_file_skipped_stats_list.append(json.dumps(stats))

        print(f"\tSUCCESS COUNT: {len(current_file_success_stats_list)}")
        print(f"\tSKIPPED COUNT: {len(current_file_skipped_stats_list)}")
        print(f"\tFAILED COUNT: {len(current_file_failed_stats_list)}")

        complete_success_list = current_file_skipped_stats_list + current_file_success_stats_list

        with open(checkpoint_file_complete_path, "w") as outfile:
            outfile.write("\n".join(complete_success_list))


