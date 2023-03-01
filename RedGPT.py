from RedGPT import FindingsGenerator


def main(args):
    FindingsGenerator.RedGPT.CreateFinding(args.api_key, args.title)

if __name__ == "__main__":
    main(FindingsGenerator.RedGPT.get_parser().parse_args())
