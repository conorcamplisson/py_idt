
from py_idt import IDTOrder

# configure output directory
IDTOrder.settings['output_dir'] = 'example_order'

def main():

    # create a new IDT oligonucleotide order
    order = IDTOrder()

    # add some oligos to this order
    order.add_oligo('Test_oligo_1', 'ACGTACGTACGTACGTACGT')
    order.add_oligo('Test_oligo_2', 'TGCATGCATGCATGCATGCATGCATGCATGCATGCATGCA', scale='250nm', purification='PAGE')
    order.add_oligo('Test_oligo_3', '/5Phos/AAAAACCCCCGGGGGTTTTT', scale='100nm', purification='HPLC')

    # create Excel IDT bulk order form
    order.save()


if __name__ == '__main__':
    main()
