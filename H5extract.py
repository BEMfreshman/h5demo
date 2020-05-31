import os
import h5py


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

    def __del__(self):

        self.outf.close()
        self.f.close()

    def __printhierachy(self):

        self.f.visititems(self.__printgroup)

    def __printgroup(self, name, node):
        if isinstance(node, h5py.Dataset):
            type = 'Table'
        else:
            type = 'Group'
        print(name + "  " + type + "  ", name.count('/'), file=self.outf)


    def h5infoprint(self):
        """
        print information in h5
        :return:
        """
        self.__printhierachy()
