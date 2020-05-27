import os
import h5py

class H5extract:

    def __init__(self, ipt):
        self.ipt = ipt
        (self.path, self.filename) = os.path.split(ipt)
        (name, extension) = os.path.splitext(self.filename)
        if extension != "h5":
            raise Exception("input file is not h5 file")

        self.outfile = self.filename + ".extracth5"
        self.f = h5py.File(self.ipt, 'r')


    def getextract(self):
        """
        print extract file
        :return:
        """

