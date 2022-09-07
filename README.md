# Repo for push_stats_app

## Create python3 venv
```
$ python3.8 -m venv .venv --prompt push-stats-venv
$ source source .venv/bin/activate
$ pip install -r requirements.txt
```

## Run App
Open a new terminal and set the current dir to push_stats_app dir
```
$ cd ./push_stats_app
$ ./scripts/run.sh
```

## Arguments:
* **input_stats_dir** - Location of the dir containing the stats file for a given day. The process will pick each file from this dir one by one for processing.
* **checkpoint_dir** - Parent dir for storing the checkpoints for each input_stats_dir. A dir will be created in this location with the same name as that of the **input_stats_dir** and then within this dir the process will store the list of successfully pushed stats from each input file. The checkpoint file for a given input file f1.json will be stored with name success-f1.json. 

## Process Description:

The process works by checking if for the given file: **f1.json** present in the **input_stats_dir** there exists a file with name **success-f1.json** in the **checkpoint_dir/{input_stats_dir_name}**. If such a file is found then the process will skip sending the stats for the brands present in this checkpoint file: **success-f1.json**, If no such file is found in the checkpoint_dir then process will try to push all the stats present in the input json file: **f1.json**. The process will apply the same logic for each file present in the **input_stats_dir** one by one.

## Clean Up For Reruns:
clean the checkpoints dir for testing with the same input stats file
```commandline
$ cd ./push_stats_app
$ rm -fr checkpoints
```