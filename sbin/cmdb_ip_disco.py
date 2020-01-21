#!/usr/bin/env python3

import argparse
from tools.disco import DiscoveryServer

def main():
    parser = argparse.ArgumentParser(description="ActiveCMDB Discovery Server")
    parser.add_argument('-i', '--ident', default='CMDB_TOOL', help='Process identifier')
    parser.add_argument('-l', '--logfile', help='Alternative logfile')
    parser.add_argument('-p', '--pidfile')
    parser.add_argument('--process', help='Stand-alone discovery')
    args = parser.parse_args()

    server = DiscoveryServer()
    if args.process:
        server.Discover(args.process)
    else:
        server.RunServer()

if __name__ = "__main__":
    main()

