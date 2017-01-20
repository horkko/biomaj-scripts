#! /usr/bin/env python
from __future__ import print_function
import sys
from biomajmanager.manager import Manager
ALLOWED_TOOLS = ['blast2', 'golden']


def main():
    """List bank and sections for a bank"""
    if len(sys.argv) < 3:
        print("Usage: %s <bank> <tool>" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    if sys.argv[2] not in ALLOWED_TOOLS:
        print("Tool %s not supported. Allowed tools: %s" % (str(sys.argv[2]), ALLOWED_TOOLS), file=sys.stderr)
        sys.exit(1)
    try:
        manager = Manager(bank=sys.argv[1])
        # {'nuc': {'dbs': ['alunuc'], 'sections': []},
        #  'pro': {'dbs': ['alupro'], 'sections': []}}
        dbs = []
        for seqtype in manager.get_bank_sections(tool=sys.argv[2]).iteritems():
            dbs.extend(seqtype[1]['dbs'])
            dbs.extend(seqtype[1]['sections'])
        print("\n".join(dbs))
    except SystemExit as err:
        print("Error occured: %s" % str(err))
        sys.exit(1)
    sys.exit(0)

# usage bm_bank_sections.py <bank> <tool>
if __name__ == '__main__':
    main()
