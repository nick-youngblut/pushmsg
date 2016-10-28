"""
IPython magic function to provide notifications via PushBullet
Author: Nicholas Youngblut <nyoungb2@gmail.com>
License: MIT
"""

from __future__ import print_function

import os
import sys
import re
import time
import IPython
from socket import gethostname
from IPython.core.magic import Magics
from IPython.core.magic import magics_class
from IPython.core.magic import line_magic
from IPython.core.magic_arguments import argument
from IPython.core.magic_arguments import magic_arguments
from IPython.core.magic_arguments import parse_argstring
from pushbullet import Pushbullet
from configparser import ConfigParser
from configparser import DuplicateSectionError
from configparser import NoSectionError

class PackageNotFoundError(Exception):
    pass


@magics_class
class PushMsg(Magics):
    """
    IPython magic function to send notifications via Pushbullet
    """
    @magic_arguments()
    @argument('msg', type=str, default=False, nargs='?',
              help='Message to send via Pushbullet')
    @argument('-n', '--name', type=str,
              help='Which API key in the pushbullet config file to use? Default: the first key')
    @argument('-a', '--add', type=str,
              help='Add an API key to your .pushbullet config file. Use syntax "KEY_NAME=o.ExASvjskasfd"')
    @argument('-l', '--list', action='store_true',
              help='List all API keys in the pushbullet config file')
    @argument('-r', '--remove', type=str,
              help='Remove one or more API keys from the pushbullet config file Provide a comma-separated list of key names')
    @argument('-p', '--path', type=str,
              help='Designate path to your pushbullet config file. Default: ~/.pushbullet')
    @argument('-h', '--hostname', action='store_true',
              help='prints the host name')

    
    @line_magic
    def pushmsg(self, line):
        """
        IPython magic function to send notifications with pushbullet
        """
        # args
        self.out = ''
        args = parse_argstring(self.pushmsg, line)
        
        # config
        ## path
        self._set_config_path(args)
        ## read/create config
        self._init_config(args)
        ## add api keys
        if args.add:
            self._key_add(args)
            return None
        ## remove api keys 
        if args.remove:
            self._key_rm(args)
            return None
        ## getting API keys
        self._key_get_all()
        ## listing API keys
        if args.list:
            self._key_list()
            return None
        ## calling pushbullet
        if args.msg:
            args.msg = args.msg.strip('"\'')
            # get specific api key
            self._key_get(args)
            # get hostname
            if args.hostname:
                args.msg = 'host:{}\n{}'.format(gethostname(), args.msg)
            # call pushbullet
            self._pushmsg(args)
            

    def _set_config_path(self, args):
        if args.path:
            self.config_path = args.path
        else:
            home_dir = os.path.expanduser('~')         
            self.config_path = os.path.join(home_dir, '.pushbullet')

    def _init_config(self, args):        
        self.push_config = ConfigParser()
        if not args.add and not os.path.isfile(self.config_path):
            raise IOError('No API key or pushbullet config file provided')
        if os.path.isfile(self.config_path):
            self.push_config.read(self.config_path)
          

    def _key_add(self, args):
        api_key = re.split('\s*[,=]\s*', args.add)
        if len(api_key) < 2:
            msg = '"{}" should be in format "KEY_NAME=KEY"'
            raise IOError(msg.format(args.add))
        try:
            self.push_config.add_section('API_keys')
        except DuplicateSectionError:
            pass                
        self.push_config.set('API_keys', api_key[0], api_key[1])
        # writing
        cfgfile = open(self.config_path, 'w')
        self.push_config.write(cfgfile)
        cfgfile.close()

    def _key_rm(self, args):
        key_names = re.split('\s*,\s*', args.remove)
        for key_name in key_names:                
            self.push_config.remove_option('API_keys',key_name)
        # writing
        cfgfile = open(self.config_path, 'w')
        self.push_config.write(cfgfile)
        cfgfile.close()

    def _key_get_all(self):
        try:
            self.api_key_names = self.push_config.options('API_keys')
        except:
            msg = '"API_keys" section in pushbullet config not found'
            raise NoSectionError(msg)

    def _key_list(self):
        for api_key_name in self.api_key_names:
            api_key = self.push_config.get('API_keys',api_key_name)
            print('API Key: {}={}'.format(api_key_name,api_key))

    def _key_get(self, args):
        if args.name:
            try:
                self.api_key = self.push_config.get('API_keys',args.name)
            except:
                msg = 'Cannot find API key "{}"'
                raise IOError(msg.format(args.name))
        else:
            try:
                self.api_key = self.push_config.get('API_keys',self.api_key_names[0])
            except:
                raise IOError('No API keys found!')

    def _pushmsg(self,args):
        pb = Pushbullet(self.api_key)
        push = pb.push_note(args.msg, '')

        
def load_ipython_extension(ipython):
    ipython.register_magics(PushMsg)

