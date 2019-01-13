#from __future__ import print_function
import Face3D as rc
import xlrd, xlwt
import os
import glob

# def RunByParams(authenticate=None,
#             enroll=None,
#             person_id=None,
#             auto_id=False,
#             reevaluate=False,
#             depth_map=None,
#             feature_map=None,
#             similarity_matrix=None,
#             roc_curve=None,
#             draw_key_points=False,
#             database='database.db',
#             parametes='K=12,N=67'):


def get_person_ids():
    limit = 7
    all_person = [os.path.basename(path)[:5] for path in os.listdir('E:/BosphorusDB/abs/')]
    return all_person[:limit]


def get_faces(person, method):
    base_folder = 'E:/BosphorusDB/abs/'

    types = ('N', 'PR', 'CR')
    list = []
    for type in types:
        mask = base_folder + person + '_filtered/*_' + type + '*_' + method + '.abs'
        faces = glob.glob(mask)
        list.extend(faces)

    return list


def enroll_method(persons, method):
    print method
    for person in persons:

        print person
        faces = get_faces(person, method)
        for face in faces:
            try:
                rc.RunByParams(enroll=face, person_id=person, database=method + '.db')
            except:
                print 'bad face %s' % face

method = 'GHA'

rc.RunByParams(roc_curve=method +'roc-curve.pdf',database=method + '.db')

# persons = get_person_ids()
#
# methods = ['GHR','BOF','M1A','BF1','MDA','MR1','MRK']
# for method in methods:
#     try:
#         enroll_method(persons, method)
#         try:
#             rc.RunByParams(roc_curve=method +'roc-curve.pdf',database=method + '.db')
#         except:
#             print 'bad method %s' % method
#     except:
#         try:
#             enroll_method(persons, method)
#             try:
#                 rc.RunByParams(roc_curve=method + 'roc-curve.pdf', database=method + '.db')
#             except:
#                 print 'bad method %s' % method
#         except:
#             print 'bad method %s' % method


# wb = xlwt.Workbook()
# ws = wb.add_sheet('Test')
# rc.RunByParams(enroll='E:/BosphorusDB/abs/bs000_filtered/bs000_N_N_0_BOF.abs', person_id='bs000', database='BOF.db')
# rc.RunByParams(enroll='E:/BosphorusDB/abs/bs000_filtered/bs000_N_N_1_BOF.abs', person_id='bs000', database='BOF.db')
#
# rc.RunByParams(enroll='E:/BosphorusDB/abs/bs104_filtered/bs104_N_N_0_BOF.abs', person_id='bs104', database='BOF.db')
# rc.RunByParams(enroll='E:/BosphorusDB/abs/bs104_filtered/bs104_N_N_1_BOF.abs', person_id='bs104', database='BOF.db')
# rc.RunByParams(enroll='E:/BosphorusDB/abs/bs104_filtered/bs104_N_N_2_BOF.abs', person_id='bs104', database='BOF.db')
# rc.RunByParams(enroll='E:/BosphorusDB/abs/bs104_filtered/bs104_N_N_3_BOF.abs', person_id='bs104', database='BOF.db')
#
#
#(c, result) = rc.RunByParams(roc_curve='E:/mm.pdf', database='BOF.db')

# for i, res in enumerate(result):
#     j = 1
#     for p, s in res:
#         ws.write(i, j, p)
#         j = j + 1
#         ws.write(i, j, s)
#         j = j + 1
#
#
# wb.save('E:/xl_rec.xls')
# #
# for i, res in enumerate(result):
#     print "bs096_N_N_0_BOF Mathod %d" % (i)
#     for p, s in res:
#         print "Match with person %s with scores %s" % (p, s)
#
# (c, result) = rc.RunByParams(authenticate='E:/BosphorusDB/abs/bs000_filtered/bs000_N_N_1_CLE.abs', database='BOF.db')
#
# for i, res in enumerate(result):
#     print "bs000_N_N_1_CLE Mathod %d" % (i)
#     for p, s in res:
#         print "Match with person %s with scores %s" % (p, s)
#
# (c, result) = rc.RunByParams(authenticate='E:/BosphorusDB/abs/bs000_filtered/bs000_N_N_0_CLE.abs', database='BOF.db')
#
# for i, res in enumerate(result):
#     print "bs000_N_N_0_CLE Mathod %d" % (i)
#     for p, s in res:
#         print "Match with person %s with scores %s" % (p, s)