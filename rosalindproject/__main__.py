import sys


def validateFilePath(PATH):
    """ validate file path """
    if not os.path.exists(PATH):
        return False
    else:
        return True

def main(args=None):
    """Main Routine"""
    if args is None:
        args = sys.argv[1:]
    if len(args) < 3:
        print("ERROR: Specify input and output file.")
    if not validateFilePath(args[1]):
        print("ERROR: Cannot find {}".format(args[1]))
        sys.exit(-1)

    rp = RosalindProject(INPUT=args[1], OUTPUT=args[2])
    rp.run()

if __name__ == "__main__":
    main()
