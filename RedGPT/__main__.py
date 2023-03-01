from .FindingsGenerator import RedGPT

def main(args):
    RedGPT.CreateFinding(args.api_key, args.title)

if __name__ == "__main__":
    main(RedGPT.get_parser().parse_args())
