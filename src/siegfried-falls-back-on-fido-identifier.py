# Title: siegfried-falls-back-on-fido-identifier
# Version: 1.0.0
# Publication date: December 5, 2024
# Publisher: NFDI4Culture
# Author: Joerg Heseler
# License: CC BY-SA 4.0

from __future__ import print_function

import os.path
import re
import json
import subprocess
import sys


############################# FIDO #############################

def file_tool(path):
    return subprocess.check_output(['file', path]).decode("utf8").strip()

class FidoFailed(Exception):
    def __init__(self, stdout, stderr, retcode):
        message = """
Fido exited {retcode} and no format was found.
stdout: {stdout}
---
stderr: {stderr}
""".format(stdout=stdout, stderr=stderr, retcode=retcode)
        super(FidoFailed, self).__init__(message)

def identify(file_):
    # The default buffer size fido uses, 256KB, is too small to be able to detect certain formats
    # Formats like office documents and Adobe Illustrator .ai files will be identified as other, less-specific formats
    # This larger buffer size is a bit slower and consumes more RAM, so some users may wish to customize this to reduce the buffer size
    # See: https://projects.artefactual.com/issues/5941, https://projects.artefactual.com/issues/5731
    cmd = ['fido', '-bufsize', '1048576',
           '-loadformats', '/usr/lib/archivematica/archivematicaCommon/externals/fido/archivematica_format_extensions.xml',
           os.path.abspath(file_)]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.decode("utf8")
    stderr = stderr.decode("utf8")

    try:
        results = stdout.split('\n')[0].split(',')
    except:
        raise FidoFailed(stdout, stderr, process.returncode)

    if process.returncode != 0 or results[-1] == '"fail"':
        raise FidoFailed(stdout, stderr, process.returncode)
    else:
        puid = results[2]
        if re.match('(.+)?fmt\/\d+', puid):
            return puid
        else:
            print("File identified as non-standard Fido code: {id}".format(id=puid), file=sys.stderr)
            return ""

############################# Siegfried #############################

class IdToolError(Exception):
    pass


class ParseError(IdToolError):
    PREFIX = 'The output produced by siegfried could not be parsed'
    def __init__(self, message=None):
        message = self.PREFIX if message is None else '{}: {}'.format(self.PREFIX, message)
        Exception.__init__(self, message)


def sf_tool(path):
    return subprocess.check_output(['sf', '-json', path]).decode("utf8")


def find_puid(sf_output):
    result = json.loads(sf_output)
    try:
        matches = result['files'][0]['matches']
    except KeyError as e:
        raise ParseError('error matching key {}'.format(e))

    if len(matches) == 0:
        raise ParseError('no matches found')

    match = matches[0]
    puid = None

    if 'puid' in match:
        puid = match['puid']
    elif 'id' in match:
        puid = match['id']
    else:
        raise ParseError

    if puid == 'UNKNOWN':
        raise IdToolError('siegfried determined that the file format is UNKNOWN')
        
        
    return puid


def identify_file(path):
    try:
        print(find_puid(sf_tool(path)))
    except IdToolError as e:
        # Siegfried could not detect file format
        try:
            print(identify(path))
            return 0
        except FidoFailed as e:
            file_output = file_tool(path)
            # FIDO can't currently identify text files with no extension, and this
            # is a common enough usecase to special-case it
            if 'text' in file_output:
                print('x-fmt/111')
            else:
                return e
        except Exception as e:
            return e
    
#        print(e, file=sys.stderr)
#        return 1
    return 0


if __name__ == '__main__':
    sys.exit(identify_file(sys.argv[1]))
