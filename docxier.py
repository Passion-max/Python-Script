import docx

# define the path to the docx file
doc_path = r"C:\Users\user\Downloads\format\CM.docx"

# define the list of dictionaries
data = [
    {'CODE': 'CM 176', 'NAME': 'IWUORAH CHALSES OBUGO', 'ADDRESS': 'UMUEZE AMAM'},
    {'CODE': 'CM 177', 'NAME': 'EDAYI ELVIS BENSON', 'ADDRESS': 'NO 1 EDAYI STREET OFF EWAH ROAD BENIN QTY EDO STATE'},
    {'CODE': 'CM 178', 'NAME': 'UFUEGBUWE EMMANUEL O.', 'ADDRESS': 'NO 1 OBI NWABUOKU AVANUE OKPANAM'},
    {'CODE': 'CM 179', 'NAME': 'NWABUINE FLORENCE NNEAMAKA', 'ADDRESS': 'AMACHAI QUARTERS, UGBOLU OSHIMILI, DELTA STATE'},
    {'CODE': 'CM 180', 'NAME': 'AYOR ROSEMARY ANINULI', 'ADDRESS': '3 ODITA STREET, AKWUFOR, ASABA'},
    {'CODE': 'CM 181', 'NAME': 'EZEBUBE EMMANUEL ELOCHUKWU', 'ADDRESS': '5 OSINA LANE AWADA OBOSI'},
    {'CODE': 'CM 182', 'NAME': 'DAVID CHISOM MARIA G.', 'ADDRESS': 'NO 5 AKPUGO CLOSE AWADA OBOSI'},
    {'CODE': 'CM 183', 'NAME': 'ONUORA RAPHEAL CHIJOKE/OGBEDO ONU', 'ADDRESS': 'UMUONU UDEJI AMECHI AWKUNANAW ENUGU STATE'},
    {'CODE': "CM 184", 'NAME': "EZEH MIRACLE OGOCHUKWU", 'ADDRESS': "NO 1 OMUONYIA STREET ACHARA LAYOUT ENUGU"},
    {'CODE': "CM 185", 'NAME': "OGBA UGOCHUKWU CALISTUS", 'ADDRESS': "NO 1 PAL JUNCTION CLOSE OKO, ORUMBA NORTH, ANAMBRA"},
    {'CODE': "CM 186", 'NAME': "BELONWU IFEOMA", 'ADDRESS': "NO 58 OZUBULU STREET FEGGE ONITSHA ANAMBRA"},
    {'CODE': "CM 187", 'NAME': "KANIFE NNEOMA MARY", 'ADDRESS': "12 OFORJINDU STREET ODEME-LAYOUT OBOSI"},
    {'CODE': "CM 188", 'NAME': "AGBODIKE AMARA ROSE", 'ADDRESS': "NO 24 OGBUFOR ROAD URUAGU NNEWI"},
    {'CODE': "CM 187", 'NAME': "KANIFE NNEOMA MARY", 'ADDRESS': "12 OFORJINDU STREET ODEME-LAYOUT OBOSI"},
    {'CODE': "CM 188", 'NAME': "AGBODIKE AMARA ROSE", 'ADDRESS': "NO 24 OGBUFOR ROAD URUAGU NNEWI"},
    {'CODE': 'CM 189', 'NAME': 'NWASIKE JANE NONYE', 'ADDRESS': 'PST. NNAMI NWASIKW COMPOUND UMRIM VILL. NAWFIA'}, 
    {'CODE': 'CM 190', 'NAME': 'NEE OBELEAGU UMEJIONU', 'ADDRESS': 'NEW HEAVEN ESTATE NKELLE EZUNAKA'},
    {'CODE': 'CM 191', 'NAME': 'IYINAGOLU OBIOMA I FRANCISCA', 'ADDRESS': 'NO 21 MMIRIKWE ROAD ABUBOR NNEWICHI NNEWI'},
    {'CODE': 'CM 192', 'NAME': 'EZEANOKWASI RITA OGOCHUKWU', 'ADDRESS': 'EKWULOBIA AGUATA LGA ANAMBRA STATE'},
    {'CODE': 'CM 193', 'NAME': 'UCHEGBE AMARACHUKWU GRACE', 'ADDRESS': 'ST THOMAS ANGLICAN CHURCH ORAUKWU'},
    {'CODE': 'CM 194', 'NAME': 'ONYEME EBELE BLESSING', 'ADDRESS': 'NO 3A EJEAGWU ESTATE AWKA'},
    {'CODE': 'CM 196', 'NAME': 'ONYEMA/UMEH THECLE CHINELO', 'ADDRESS': 'EDUCATION AUTHORITY ORUMBA NORTH LGA, ANAMBRA'},
    {'CODE':"CM 197", 'NAME':"IKE GRACE NGOZI", 'ADDRESS':"ENGR. IKE IKENNA JULIUS COMP. UMUCHIANA-EKWULOBIA"},
    {'CODE':"CM 198", 'NAME':"NWOGWUGWU CHIKEZIE ZARCUS", 'ADDRESS':"APARACHI MBAUKWU IHITTE EZINIFITTE IMO STATE"},
    {'CODE':"CM 199", 'NAME':"NWAGWU ALEX ANAMBRA", 'ADDRESS':"SCS/53 DAN ANYIM STADUIM OWERRI IMO STATE"},
    {'CODE':"CM 200", 'NAME':"AKOR AGNESS ADAOBI", 'ADDRESS':"IKENNA OKONKWO HOUSE AKAGO – UKWU URUAGU NNEWI"}
    ]
# open the docx file
doc = docx.Document(doc_path)

# get the size of the data list
data_size = len(data)
ct = True

# loop through each page in the document
for page_id in range(data_size):
    # get the dictionary from the data list using the current index
    current_dict = data[page_id]
    
    # loop through each paragraph in the current page
    for para in doc.paragraphs:
        # replace the placeholders with the values from the dictionary
        para.text = para.text.replace('[CODE]', current_dict['CODE'])
        para.text = para.text.replace('[NAME]', current_dict['NAME'])
        para.text = para.text.replace('[ADDRESS]', current_dict['ADDRESS'])
        break

# save the modified document
doc.save(doc_path)

