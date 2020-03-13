# !/usr/bin/env python3

import xml.etree.ElementTree as ET
import difflib

""" Returns the difference between the given two XML files.

    Parameters:
        file_path_1: Location of the first XML file.
        file_path_2: Location of the second XML file.
        print_output: Used as a flag

    Returns:
        comparision(List):The List which contains the tags and values.   

"""


def files_equal(file_path_1, file_path_2, nested_compare=False, print_output=False):
    tree1 = ET.parse(file_path_1)
    tree2 = ET.parse(file_path_2)

    root1 = tree1.getroot()
    root2 = tree1.getroot()

    # print((tree1.getroot()).tag)
    # print((tree2.getroot()).tag)

    # for child in root1:
    #     print(child.tag, child.attrib)
    #
    # for child in root1.iter('ClCompile'):
    #     print(ET.tostring(child))

    e1 = tree1
    string1 = ""
    list1 = []
    for elt in e1.iter():
        # print(str(elt.tag) + " : " + str(elt.text))
        s = str(elt.tag) + " : " + str(elt.text)
        list1.append(' '.join(s.split()))
        # string1 = string1 + str(elt.tag) + " : " + str(elt.text)

    e2 = tree2
    string2 = ""
    list2 = []
    for elt in e2.iter():
        # print(elt)
        # print(str(elt.tag) + " : " + str(elt.text))
        s = str(elt.tag) + " : " + str(elt.text)
        list2.append(' '.join(s.split()))
        # string2 = string2 + str(elt.tag) + " : " + str(elt.text)

    # print(list1)
    # print(list2)

    if print_output:
        print(list(set(list1) - set(list2)))

    if len(list(set(list1) - set(list2))) == 0:
        return True

    return False


files_equal('C:/Users/graju/PycharmProjects/xmlCompare/small_file_source.xml',
            'C:/Users/graju/PycharmProjects/xmlCompare/small_file_compare.xml', False, True)
