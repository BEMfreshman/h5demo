import sys
import getopt
from H5demo import H5demo


def help():
    print("Usage: python demo.py [-h][-i]")
    print("-h,help: get how to use this function")
    print("-i,input: input h5 file name")


def main(argv):
    """

    :param argv: input arguments
    :return:
    """

    inputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:", ["help", "inputfile="])
    except getopt.GetoptError:
        print("Error: Fail to launch program")
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg

    print("inputfile is:", inputfile)

    h5demo = H5demo(inputfile)
    h5demo.h5infoprint()


if __name__ == "__main__":
    main(sys.argv[1:])
