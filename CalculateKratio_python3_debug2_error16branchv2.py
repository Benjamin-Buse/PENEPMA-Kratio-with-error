#! python3

from tkinter import *
from tkinter import filedialog
import csv
import math
element = []
energy = []
intensity = []
uncert = []
TotalInt = []
TotalUnc = []
combE = []
combI = []
combU = []
combTI = []
combTU = []
combFile = []
ElementNo = []
StdcombE = []
StdcombI = []
StdcombU = []
StdcombTI = []
StdcombTU = []
StdcombFile = []
StdElementNo = []
Kraw = []
KrawErr = []
TotalKraw = []
TKrawErr = []
KStdNo = []
KSamNo = []
KStdFile = []
KSamFile = []
KSamFileNew = []
SamFName = []
StdFName = []
sam = input("enter number of unknown samples: ")
num = input("enter number of elements: ")
for i in range(int(num)):
	element.append(0)
	energy.append(0)
	intensity.append(0)
	uncert.append(0)
	TotalInt.append(0)
	TotalUnc.append(0)
for i in range(int(num)):
	element[i] = input("enter element 1 as IZS0S1: no spaces; e.g. 32L3M5 is Ge La1 or 13KL3 is Al Ka1: ")	

##print("Select unknown pe-intens-XX.dat file (enter each unknown seperately)")
for x in range(int(sam)):
	file_path_string = filedialog.askopenfilename()
	SamFName.append(file_path_string)
	f = open(file_path_string)
	csv_reader = csv.reader(f, delimiter=' ')
	for row in csv_reader:
		array = row
		##print("Len(array)")
		##print(len(array))
		if len(array) > 5:
			negshift = 0 if array[4] == '' else 1
			##print("negshift: ",negshift)
			###print('kid' if array[4] == '' else 'adult')
			test = array[3]+array[5-negshift]+array[6-negshift]
			##print("test: ", test)
			###print("element[i]: ", element[i])
			for i in range(int(num)):
				if test == element[i]:
					energy[i] = array[8-negshift]
					##print("Energy[i]: ",energy[i])
					intensity[i] = array[10-negshift]
					uncert[i] = array[11-negshift]
					TotalInt[i] = array[22-negshift]
					TotalUnc[i] = array[23-negshift]
					combE.append(energy[i])
					combI.append(intensity[i])
					combU.append(uncert[i])
					combTI.append(TotalInt[i])
					combTU.append(TotalUnc[i])
					combFile.append(file_path_string)
					ElementNo.append(element[i])
					
std = input("enter number of standard samples: ")

##print("Select standard pe-intens-XX.dat file (enter each standard seperately)")
for x in range(int(std)):
	file_path_string = filedialog.askopenfilename()
	StdFName.append(file_path_string)
	f = open(file_path_string)
	csv_reader = csv.reader(f, delimiter=' ')
	for row in csv_reader:
		array = row
		if len(array) > 5:
			negshift = 0 if array[4] == '' else 1
			##print("negshift: ",negshift)
			test = array[3]+array[5-negshift]+array[6-negshift]
			for i in range(int(num)):
				if test == element[i]:
					energy[i] = array[8-negshift]
					##print("energy[i]: ",energy[i])
					intensity[i] = array[10-negshift]
					uncert[i] = array[11-negshift]
					TotalInt[i] = array[22-negshift]
					TotalUnc[i] = array[23-negshift]
					StdcombE.append(energy[i])
					StdcombI.append(intensity[i])
					StdcombU.append(uncert[i])
					StdcombTI.append(TotalInt[i])
					StdcombTU.append(TotalUnc[i])
					StdcombFile.append(file_path_string)
					StdElementNo.append(element[i])
					
Kraw.append("K-ratio")
TotalKraw.append("Total K-ratio")
KSamNo.append("Element")
KStdNo.append("Element")
KStdFile.append("Standard file")
KSamFile.append("Sample file")
KSamFileNew.append("Sample file New")
KrawErr.append("K-ratio Error")
TKrawErr.append("Tot K-ratio Error")
for x in range(len(combFile)):
        for i in range(len(StdcombFile)):
                if ElementNo[x] == StdElementNo[i]:
                        calcKraw = float(combI[x])/float(StdcombI[i])
                        ##print("combU: ", combU[x], "stdcombU: ", StdcombU[i])
                        err = calcKraw*math.sqrt(math.pow((float(combU[x])/float(combI[x])),2)+math.pow((float(StdcombU[i])/float(StdcombI[i])),2))
                        ##print(calcKraw)
                        calcTotKraw = float(combTI[x])/float(StdcombTI[i])
                        ##print("combTU: ", combTU[x]," StdcombTU: ", StdcombTU[i])
                        Terr = calcTotKraw*math.sqrt(math.pow((float(combTU[x])/float(combTI[x])),2)+math.pow((float(StdcombTU[i])/float(StdcombTI[i])),2))
                        ##print("Terr: ", Terr)
                        ##print(calcTotKraw)
                        Kraw.append(calcKraw)
                        KrawErr.append(err)
                        TotalKraw.append(calcTotKraw)
                        TKrawErr.append(Terr)
                        KStdFile.append(StdcombFile[i][3:])
                        KSamFile.append(combFile[x][3:])
                        KSamFileNew.append(combFile[x])
                        KStdNo.append(StdElementNo[i])
                        KSamNo.append(ElementNo[x])
                        #print("x: ", x)
                        #print("i: ", i)
                        #print((combFile[x][3:]))
                        #print((combFile[x]))
                        #print((StdcombFile[i][3:]))
                        #print("KSamFileNew: ",KSamFileNew)
                        #print("KSamFile: ",KSamFile)
ReK = []
ReKE = []
ReTK = []
ReTKE = []
ReEl = []
ReStd = []
ReUnkFile = []
for i in range(int(sam)):
	ReK.append(0)
	ReKE.append(0)
	ReTK.append(0)
	ReTKE.append(0)
	ReEl.append(0)
	ReStd.append(0)
	ReUnkFile.append(0)
KrawOrder = []
KrawErrOrder = []
TKrawOrder = []
TKrawErrOrder = []
SamElOrder = []
StdOrder = []
UnkFileTitle = []
for x in range(int(sam)):
        for i in range(len(Kraw)):
                if SamFName[x][3:] == KSamFile[i]:
                        KrawOrder.append(Kraw[i])
                        UnkFileTitle.append(KSamFileNew[i])
                        KrawErrOrder.append(KrawErr[i])
                        TKrawOrder.append(TotalKraw[i])
                        TKrawErrOrder.append(TKrawErr[i])
                        SamElOrder.append(KSamNo[i])
                        StdOrder.append(KStdFile[i])
        ReK[x] = KrawOrder
        ReUnkFile[x] = UnkFileTitle
        ReKE[x] = KrawErrOrder
        ##print(KrawOrder)
        ##print(ReK[x])
        ReTK[x] = TKrawOrder
        ReTKE[x] = TKrawErrOrder
        ReEl[x] = SamElOrder
        ReStd[x] = StdOrder
        KrawOrder = []
        KrawErrOrder = []
        TKrawOrder = []
        TKrawErrOrder = []
        SamElOrder = []
        StdOrder = []
##print("Select location and name of results file")

f3 = filedialog.asksaveasfile(mode='w', defaultextension='csv')
resu=csv.writer(f3)
ReKTitle = "Kratio (exc. flourescence)"
ReUnkFileTitle = "Unknown file title"
ReKErrTitle = "Kratio (exc. Fl) Error"
ReTKTitle = "Kratio (flourescence inc.)"
ReTKErrTitle = "Kratio (inc. Fl) Error"
ReELTitle = "Element"
ReStdTitle = "Standard"
LineUnkFileTitle = []
LineMake = []
LineMakeErr = []
LineMaking = []
LineMakingErr = []
LineTwo = []
LineThree = []
FileTitle = "File"
FileNewLine = "KSamFileNew"
for x in range(len(ReK)):
        LineMake.append(0)
        LineUnkFileTitle.append(0)
        LineMakeErr.append(0)
        LineMaking.append(0)
        LineMakingErr.append(0)
        LineTwo.append(0)
        LineThree.append(0)
        FileT = []
        FileT.append(FileTitle)
        FileT.append(str(SamFName[x]))
        FileN = []
        FileN.append(FileNewLine)
        FileN.append(str(KSamFileNew[x]))
        LineUnkFileTitle[x] = [ReUnkFileTitle] + ReUnkFile[x]
        LineMake[x] = [ReKTitle] + ReK[x]
        LineMakeErr[x] = [ReKErrTitle] + ReKE[x]
        LineMaking[x] = [ReTKTitle] + ReTK[x]
        LineMakingErr[x] = [ReTKErrTitle] + ReTKE[x]
        LineTwo[x] = [ReELTitle] + ReEl[x]
        LineThree[x] = [ReStdTitle] + ReStd[x]
        resu.writerow(FileT)
        #resu.writerow(FileN)
        #resu.writerow(KSamFileNew)
        #resu.writerow(LineUnkFileTitle[x])
        resu.writerow(LineTwo[x])
        resu.writerow(LineMake[x])
        resu.writerow(LineMakeErr[x])
        resu.writerow(LineMaking[x])
        resu.writerow(LineMakingErr[x])
        resu.writerow(LineThree[x])
        resu.writerow("")
f3.close()
