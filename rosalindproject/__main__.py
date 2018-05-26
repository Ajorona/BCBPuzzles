import os, sys
from rosalindproject import RosalindProject

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
    if len(args) < 2:
        print("ERROR: Specify input and output file.")
    if not validateFilePath(args[0]):
        print("ERROR: Cannot find {}".format(args[0]))
        sys.exit(-1)

    rp = RosalindProject(INPUT=args[0], OUTPUT=args[1])
    rp.run()

if __name__ == "__main__":
    main()
