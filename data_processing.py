import os
from collections import defaultdict
import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings("ignore")

root = "NSL-KDD-Dataset"

train_file = os.path.join(root, "KDDTrain+.txt")
test_file = os.path.join(root, "KDDTest+.txt")

headers = [
    "duration", "protocol_type", "service", "flag",
    "src_bytes", "dst_bytes", "land", "wrong_fragment",
    "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted",
    "num_root", "num_file_creations", "num_shells", "num_access_files",
    "num_outbound_cmds", "is_host_login", "is_guest_login", "count",
    "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate",
    "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
    "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
    "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "attack_type",
    "success_pred"
]

columns = np.array(headers)

nominal_ids = [1, 2, 3]
binary_ids = [6, 11, 13, 14, 20, 21]
numeric_ids = list(set(range(41)).difference(nominal_ids).difference(binary_ids))

nominal_columns = columns[nominal_ids].tolist()
binary_columns = columns[binary_ids].tolist()
numeric_columns = columns[numeric_ids].tolist()

category = defaultdict(list)
category["benign"].append("normal")

with open("NSL-KDD-Dataset/training_attack_types.txt", "r") as f:
    for line in f.readlines():
        attack, cat = line.strip().split(" ")
        category[cat].append(attack)

attack_mapping = dict((v, k) for k in category for v in category[k])

train_data = pd.read_csv(train_file, names=headers)
test_data = pd.read_csv(test_file, names=headers)

train_data["attack_category"] = train_data["attack_type"].map(lambda x: attack_mapping[x])
train_data.drop(["success_pred"], axis=1, inplace=True)

test_data["attack_category"] = test_data["attack_type"].map(lambda x: attack_mapping[x])
test_data.drop(["success_pred"], axis=1, inplace=True)

print(train_data.shape)
print(test_data.shape)

print("Saving...")

train_data.to_csv("train-data.csv", index=False)
test_data.to_csv("test-data.csv", index=False)