
import argparse
import src.compute

def main():
    global global_url
    global global_seconds
    global global_method
    _description="Bypass-http is a python tool to automatise bypass of 403 and 401 HTTP error."

    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument("-i", help="IP of the target", required=True)
    parser.add_argument("-a", help="PATH of the target", required=True)
    parser.add_argument("-p", help="PORT of the target, 80 by default", default=80)
    parser.add_argument("-v", help="VERSION of the target, HTTPS/2.0 by default", default="HTTPS/2.0")
    parser.add_argument("-m", help="METHOD of the inital error, GET by default", default="GET")
    parser.add_argument("-s", help="SECONDS between each request sent, 1 by default", default=1)
    args = parser.parse_args()

    print("______                             _     _   _          \n\
| ___ \                           | |   | | | |        \n\
| |_/ /_   _ _ __   __ _ ___ ___  | |__ | |_| |_ _ __  \n\
| ___ \ | | | '_ \ / _` / __/ __| | '_ \| __| __| '_ \ \n\
| |_/ / |_| | |_) | (_| \__ \__ \ | | | | |_| |_| |_) |\n\
\____/ \__, | .__/ \__,_|___/___/ |_| |_|\__|\__| .__/ \n\
        __/ | |               ______            | |    \n\
       |___/|_|              |______|           |_|    \n\n\
403 & 401 bypass tool, to use with the authorization of the target.\n\
Created by Reinhardt\n\n")

    src.compute.run_exploits(args.i, int(args.p), args.a, args.v, args.m, float(args.s))

if __name__ == "__main__":
    main()
