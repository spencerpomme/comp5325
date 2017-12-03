# dist_bank_resources.py
"""
The balance data json utiliztion code.
"""

import json
# import dist_bank_pb2
# from dist_bank_exceptions import *

from . import dist_bank_pb2
from .dist_bank_exceptions import *

_SUCCESS_MODIFIED = 0
_MODIFICATION_ERR = 1
_NOT_ENOUGH_MONEY = 2


def read_dist_bank_database():
    """
    Reads the dist bank database.

    Returns:
        he full contents of the dist bank database as a sequence of
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


def modify_dist_bank_database_withdraw(request):
    """
    Modifies dist bank database upon withdraw operation.

    # Remark: Do we need to keep track of the modifications?
    request: <class 'dist_bank_pb2.WithdrawRequest'> or <class 'dist_bank_pb2.SaveRequest'>
    returns: bool
    """
    try:
        dist_bank_db_file = open("dist_bank_db.json", "r")
        db = json.load(dist_bank_db_file)
        print('bf wd-->', db[66])
        for i in range(len(db)):
            if db[i]["uid"] == request.uid:
                if float(db[i]["balance"]) >= request.with_amount:
                    db[i].update({"balance": str(float(db[i]["balance"]) - request.with_amount)})
                    break
                else:
                    return _NOT_ENOUGH_MONEY
        print('af wd-->', db[66])
        dist_bank_db_file.close()
        dist_bank_db_file = open("dist_bank_db.json", "w")
        json.dump(db, dist_bank_db_file)
    except:
        return _MODIFICATION_ERR
    else:
        return _SUCCESS_MODIFIED
    finally:
        dist_bank_db_file.close()

def modify_dist_bank_database_save(request):
    """
    Modifies dist bank database upon save operation.

    # Remark: Do we need to keep track of the modifications?
    request: <class 'dist_bank_pb2.WithdrawRequest'> or <class 'dist_bank_pb2.SaveRequest'>
    returns: bool
    """
    try:
        dist_bank_db_file = open("dist_bank_db.json", "r")
        db = json.load(dist_bank_db_file)
        print('bf sv-->', db[66])
        for i in range(len(db)):
            if db[i]["uid"] == request.uid:
                db[i].update({"balance": str(float(db[i]["balance"]) + request.save_amount)})
        print('af sv-->', db[66])
        dist_bank_db_file.close()
        dist_bank_db_file = open("dist_bank_db.json", "w")
        json.dump(db, dist_bank_db_file)
    except:
        return _MODIFICATION_ERR
    else:
        return _SUCCESS_MODIFIED
    finally:
        dist_bank_db_file.close()


if __name__ == "__main__":

    import time
    print("Testing withdraw: ")
    modify_dist_bank_database_withdraw(dist_bank_pb2.WithdrawRequest(uid="5a221afc4fcb9e8932acaf8b", with_amount=94274.05))
    print('\n')
    time.sleep(5)
    print("Testing save: ")
    modify_dist_bank_database_save(dist_bank_pb2.SaveRequest(uid="5a221afc4fcb9e8932acaf8b", save_amount=94274.05))
