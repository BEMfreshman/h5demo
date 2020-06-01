import os
import h5py
import math


class H5demo:

    def __init__(self, ipt):
        self.ipt = ipt
        (self.path, self.filename) = os.path.split(ipt)
        (name, extension) = os.path.splitext(self.filename)
        if extension != ".h5":
            raise Exception("input file is not h5 file")

        self.outfile = self.filename + ".extracth5"
        self.outf = open(self.outfile, mode='w', encoding='utf-8')

        self.f = h5py.File(self.ipt, 'r')

        self.tbllist = []

    def __del__(self):

        self.outf.close()
        self.f.close()

    def __printname(self):
        print("Name", file=self.outf)
        self.f.visititems(self.__printgroup)

    def __printgroup(self, name, node):
        if isinstance(node, h5py.Dataset):
            type = 'Table'
            self.tbllist.append(name)
        else:
            type = 'Group'
        print(name + "  " + type, file=self.outf)

    def __printdata(self):
        if len(self.tbllist) == 0:
            return
        print("Data", file=self.outf)

#        permittedkeyword = {"DISPLACEMENT","EIGENVECTOR","DOMAINS","MPC_FORCE","SPC_FORCE","GRID_FORCE",""}

        for item in self.tbllist:

            tbl = self.f[item]
            print(tbl.name, file=self.outf)
            if isinstance(tbl, h5py.Dataset):
                row = tbl.shape[0]
                col = len(tbl[()][0])
                if row == 1:
                    if col == 1:
                        print(tbl[()][0][0], file=self.outf)
                    else:
                        for j in (0, math.floor(col/2), col-1):
                            print(tbl[()][0][j], file=self.outf)
                else:
                    for i in (0, math.floor(row/2), row-1):
                        if col == 1:
                            print(tbl[()][i][0], file=self.outf)
                        else:
                            for j in (0, math.floor(col/2), col-1):
                                print(tbl[()][i][j], file=self.outf)

    def h5infoprint(self):
        """
        print information in h5
        :return:
        """
        self.__printname()
        self.__printdata()
