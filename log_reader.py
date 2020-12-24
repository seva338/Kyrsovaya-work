# !/usr/bin/env python3
import subprocess


def all_logs(path):
    log = subprocess.check_output(['tail', '-n','+0', path])
    out = log.decode('utf-8')
    return ''.join(out)


def last_log(path):
    log = subprocess.check_output(['tail', '-n','1', path])
    out = log.decode('utf-8')
    return ''.join(out)
