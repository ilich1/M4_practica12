import xml.etree.ElementTree as ET
#IMPORTEM XML
#CREEM UNA FUNCIÓ QUE CREA Y MOSTRA UN ARXIU XML
def practica12A():
    p = ET.Element('students')
    c1 = ET.SubElement(p, 'student')
    c2 = ET.SubElement(p, 'student')
    c3 = ET.SubElement(p, 'student')
    c4 = ET.SubElement(p, 'student')
    c5 = ET.SubElement(p, 'student')
    sc1 = ET.SubElement(c1, 'name')
    sc11 = ET.SubElement(c1, 'surname')
    sc12 = ET.SubElement(c1, 'email')
    sc13 = ET.SubElement(c1, 'dni')
    sc1.text = "Bader"
    sc11.text = "Hammani"
    sc12.text = "Bader@gmail.com"
    sc13.text = "12345678L"
    sc2 = ET.SubElement(c2, 'name')
    sc21 = ET.SubElement(c2, 'surname')
    sc22 = ET.SubElement(c2, 'email')
    sc23 = ET.SubElement(c2, 'dni')
    sc2.text = "Angelo"
    sc21.text = "Yachi"
    sc22.text = "Angelo@gmail.com"
    sc23.text = "15345678L"
    sc3 = ET.SubElement(c3, 'name')
    sc31 = ET.SubElement(c3, 'surname')
    sc32 = ET.SubElement(c3, 'email')
    sc33 = ET.SubElement(c3, 'dni')
    sc3.text = "Ilich"
    sc31.text = "Tovar"
    sc32.text = "Ilich@gmail.com"
    sc33.text = "16345678L"
    sc4 = ET.SubElement(c4, 'name')
    sc41 = ET.SubElement(c4, 'surname')
    sc42 = ET.SubElement(c4, 'email')
    sc43 = ET.SubElement(c4, 'dni')
    sc4.text = "Bilal"
    sc41.text = "Bilal"
    sc42.text = "Bilal@gmail.com"
    sc43.text = "17345678L"
    sc5 = ET.SubElement(c5, 'name')
    sc51 = ET.SubElement(c5, 'surname')
    sc52 = ET.SubElement(c5, 'email')
    sc53 = ET.SubElement(c5, 'dni')
    sc5.text = "Arnau"
    sc51.text = "Rodri"
    sc52.text = "Arnau@gmail.com"
    sc53.text = "19345678L"

    ET.indent(p)
    students = ET.ElementTree(p)
    root = students.getroot()
    #BUCLE PER CREAR ELS ATRIBUTS
    for element in root:
        element.set('type', 'programmer')

    students.write('practica12A.xml')

    root = students.parse('practica12A.xml')
    #MOSTREM L'ARXIU XML
    ET.dump(root)


practica12A()
