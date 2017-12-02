# dist_bank_resources.py
"""
The balance data json utiliztion code.
"""

import json

import dist_bank_pb2


def read_dist_bank_database():
    """Reads the dist bank database.

    Returns:
      The full contents of the dist bank database as a sequence of
        dist_bank_pb2.BalanceRecord.
    """
    record_list = []
    with open("dist_bank_db.json") as dist_bank_db_file:
        for item in json.load(dist_bank_db_file):
            record = dist_bank_pb2.BalanceRecord(
                uid=item["uid"],
                index=item["index"],
                # Balance field is a string in json, so change to float:
                balance=float(item["balance"]))
            record_list.append(record)
    return record_list