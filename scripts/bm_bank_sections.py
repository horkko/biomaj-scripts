#! /usr/bin/env python
from __future__ import print_function
import os
import sys
try:
    from biomajmanager.manager import Manager
except ImportError as err:
    print("Please install 'biomajmanager' package. See https://github.com/horkko/biomaj-manager")
    sys.exit(1)

ALLOWED_TOOLS = ['blast2', 'golden']


def main(args):
    """List bank and sections for a bank"""
    if len(args) < 2:
        print("Usage: %s <bank> <tool>" % os.path.basename(__name__), file=sys.stderr)
        sys.exit(1)
    if args[1] not in ALLOWED_TOOLS:
        print("Tool '%s' not supported. Allowed tools: %s" % (str(args[1]), ALLOWED_TOOLS), file=sys.stderr)
        sys.exit(1)
    try:
        manager = Manager(bank=args[0])
        # {'nuc': {'dbs': ['alunuc'], 'sections': []},
        #  'pro': {'dbs': ['alupro'], 'sections': []}}
        dbs = []

        for seqtype in manager.get_bank_sections(tool=args[1]).iteritems():
            dbs.extend(seqtype[1]['dbs'])
            dbs.extend(seqtype[1]['sections'])
        print("\n".join(dbs))
    except SystemExit as err:
        print("Error occured: %s" % str(err), file=sys.stderr)
        sys.exit(1)

# usage bm_bank_sections.py <bank> <tool>
if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)
