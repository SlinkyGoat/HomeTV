import subprocess

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('tv_controls', __name__, url_prefix='/tv-controls')

is_tv_on = False

@bp.route('/turn_on', methods=('GET', 'POST'))
def turn_on():
    # subprocess.run(["echo", "on 0", "|", "cec-client", "-s", "-d", "1"])
    subprocess.run(["echo on 0 | cec-client -s -d 1"], shell=True)
    is_tv_on = True
    return ''

@bp.route('/turn_off', methods=('GET', 'POST'))
def turn_off():
    # subprocess.run(["echo", "standby 0", "|", "cec-client", "-s", "-d", "1"])
    subprocess.run(["echo standby 0 | cec-client -s -d 1"], shell=True)
    is_tv_on = False
    return ''
