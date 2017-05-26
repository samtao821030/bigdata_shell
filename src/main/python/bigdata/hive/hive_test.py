import os,sys,datetime,time

def hive_table_create():
    print("#--------------start create hive table #")
    hive_command="""
        hive -e "
            create external table if not exist 
        "
    """