#!/usr/bin/env python3

import os
import platform
import yaml
import re
#import Configparser
from subprocess import check_call,check_output,CalledProcessError

from charmhelpers import fetch
#from charmhelpers.core import host
from charmhelpers.core import hookenv
from charmhelpers.core.hookenv import log
# log level: CRITICAL,ERROR,WARNING,INFO,DEBUG
from charmhelpers.core.hookenv import CRITICAL
from charmhelpers.core.hookenv import ERROR
from charmhelpers.core.hookenv import WARNING
from charmhelpers.core.hookenv import INFO
from charmhelpers.core.hookenv import DEBUG


from charms.reactive.helpers import is_state
from charms.reactive.bus import set_state
from charms.reactive.bus import get_state
from charms.reactive.bus import remove_state
from charms.reactive import when
from charms.reactive import when_not

from charms.layer.hpccsystems_platform import HPCCSystemsPlatformConfig

@when('platform.installed')
@when_not('platform.configured')
@when_not('platform.started')
def configure_platform():
    platform = HPCCSystemsPlatformConfig()
    platform.open_ports()
    set_state('platform.configured')

# @when_not('platform.configured')?????
@when('platform.configured')
@when_not('platform.started')
@when_not('platform.start.failed')
def start_platform():
    remove_state('platform.started')
    remove_state('platform.start.failed')
    platform = HPCCSystemsPlatformConfig()
    if platform.start():
       set_state('platform.start.failed')
       hookenv.status_set('blocked', 'hpcc start failed')
    else:
       set_state('platform.started')
       hookenv.status_set('active', 'started')

@when('hpcc-esp.available')     
def configure_esp(http):
    http.configure(8010)
