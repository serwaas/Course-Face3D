#from __future__ import print_function
import Face3D as rc
#import xlrd, xlwt
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
    all_person = [os.path.basename(path)[:5] for path in os.listdir('E:/BosphorusDB/abs/')]
    return all_person


def get_faces(person, method):
    base_folder = 'E:/BosphorusDB/abs/'

    mask = base_folder + person + '_filtered/*_' + method + '.abs'
    faces = glob.glob(mask)

    return faces

def get_person_folder(person):
    base_folder = 'E:/BosphorusDB/abs/'

    return base_folder + person + '_filtered/'


def enroll_method(persons, method):
    print method

    dbName = 'FullBase'

    for person in persons:
        print person
        person_folder = get_person_folder(person)
        print dbName
        enroll_faces(person, person_folder, dbName, method)
        copy_to_dbs(person, dbName, method)


def copy_to_dbs(person_id, dbFrom, method):
    dbs = [
        ['Face', ['N', 'LFAU', 'UFAU', 'CAU', 'E']],
        ['FaceOcclusion', ['N', 'LFAU', 'UFAU', 'CAU', 'E', 'O']],
        ['FacePitchRotation', ['N', 'LFAU', 'UFAU', 'CAU', 'E', 'PR']],

        ['Rotation', ['YR', 'CR', 'PR']]
    ]

    db_from_path = './db/' + method + '_' + dbFrom + '.db'
    for dbName, masks in dbs:
        for mask in masks:
            try:
                rc.RunByParams(copy_to_database='./db/' + method + '_' + dbName + '.db',
                               mask='_' + mask + '_',
                               database=db_from_path)
            except:
                print 'bad face %s' % person_id


def enroll_faces(person_id, folder, db_name, method):

    try:
        rc.RunByParams(enroll=folder, person_id=person_id, database='./db/' + method + '_' + db_name + '.db', mask=method)
    except:
        print 'bad face %s' % person_id


def get_faces_for_db(faces, masks):
    result = []
    for mask in masks:
        result.extend([f for f in faces if ('_' + mask + '_') in f])

    return result


persons = get_person_ids()

methods = ['CLE', 'MDM', 'MMF', 'MDR', 'M1R', 'M1M', 'GHA', 'GHM', 'GHR', 'BOF', 'M1A', 'BF1', 'MDA', 'MR1', 'MRK']
for method in methods:
    try:
        enroll_method(persons, method)
        # try:
        #     rc.RunByParams(roc_curve='./roc/' + method + 'roc-curve.pdf', database=method + '.db')
        # except:
        #     print 'bad method %s' % method
    except:
        print 'very bad method %s' % method



#enroll_faces('bs045', ['C:/Users/SW/Music/CSU/abs/'], 'test')
# rc.RunByParams(enroll='C:/Users/SW/Music/CSU/abs/', person_id='bs045', database='./db/' + 'test1' + '.db', mask='CLE')
# rc.RunByParams(copy_to_database='Test_n1', mask='_N_N_1_', database='./db/' + 'test' + '.db')

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