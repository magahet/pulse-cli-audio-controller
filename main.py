import pulsectl
import argparse
from tabulate import tabulate


def main(args):
    attribute = None
    value = None

    if args.name:
        attribute = "name"
        value = args.name
    elif args.desc:
        attribute = "description"
        value = args.desc
    elif args.index:
        attribute = "index"
        value = args.index

    with pulsectl.Pulse("audio-switcher") as pulse:
        if attribute:
            for sink in pulse.sink_list():
                if getattr(sink, attribute) == value:
                    pulse.default_set(sink)
                    break
            else:
                print("Sink not found")

        rows = [
            [s.index, s.name, s.description, s.state._value] for s in pulse.sink_list()
        ]
        headers = ["Index", "Name", "Description", "State"]
        table = tabulate(rows, headers=headers, tablefmt="plain")
        print(table)
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Switch audio output")
    parser.add_argument(
        "--name", "-n", metavar="name", type=str, help="Sink name to switch to"
    )
    parser.add_argument(
        "--desc", "-d", metavar="desc", type=str, help="Sink description to switch to"
    )
    parser.add_argument(
        "--index", "-i", metavar="index", type=int, help="Sink index to switch to"
    )
    args = parser.parse_args()

    main(args)
