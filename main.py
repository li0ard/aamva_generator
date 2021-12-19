def gen(lastName, middleName, firstName, gender, state, iin, street, city, zip, dob, expire, issue, licNum, classif, revision, restriction, endorsenet, discriminator, inventory, audit, eyes, hairs, feet, in_, weight, veteran, organDonor):
	header = "@\x0A\x1E\x0D"
	oheader = "@\\n\\x1E\\n"
	filetype = "ANSI "
	version = "09"
	jurVer = "00"
	entries = "01"
	subType = "DL"
	offset = "XXXX"
	lengthField = "XXXX"
	compliance = "F"

	formattedlastName = str.upper(lastName)
	formattedmiddleName = str.upper(middleName)
	formattedfirstName = str.upper(firstName)

	height = (int(feet) * 12) + int(in_)
	height = "0" + str(height) + " in"

	if int(weight) <= 99:
		weight = "0" + weight
	if gender == "m":
		genderFormated = "1"
	else:
		genderFormated = "2"
	while len(zip) < 9:
		zip = zip + "0"
	FlagRestriction = False;
	if len(restriction) > 0:
		FlagRestriction = True
	FlagEndosernent = False;
	if len(endorsenet) > 0:
		FlagEndosernent = True

	offset = len(header) + len(filetype) + len(iin) + len(version) + len(jurVer) + len(entries) + len(subType) + len(offset) + len(lengthField)
	formattedOffset = "00" + str(offset)

	lengthField = len(subType) + len("DAQ") + len(str(licNum)) + len("\x0ADCS") + len(formattedlastName) + len("\x0ADDEN\x0ADAC") + len(formattedfirstName) + len("\x0ADDFN\x0ADAD") + len(formattedmiddleName) + len("\x0ADDGN\x0ADCA") + len(classif) + len("\x0ADCBNONE\x0ADCDNONE\x0ADBA") +len(expire) + len("\x0ADBD") + len(issue) + len("\x0ADBB") + len(dob) + len("\x0ADBC") + len(genderFormated) + len("\x0ADAY") + len(eyes) + len("\x0ADAZ") + len(hairs) + len("\x0ADAU") + len(height) + len("\x0ADAG") + len(street) + len("\x0ADAI") + len(city) + len("\x0ADAJ") + len(state) + len("\x0ADAK") + len(zip) + len("\x0ADCF") + len(discriminator) + len("\x0ADCGUSA\x0ADCJ") + len(audit) + len("\x0ADCK") + len(inventory) + len("\x0ADDA") + len(compliance) + len("\x0ADDB") + len(revision)

	if veteran:
		lengthField = lengthField + 1 + len("\x0ADDL")
	if organDonor:
		lengthField = lengthField + 1 + len("\x0ADDK")
	if FlagRestriction:
		lengthField = lengthField + len(restriction) + len("\x0ADCB")
	if (FlagEndosernent):
		lengthField = lengthField + len(endorsenet) + len("\x0ADCD")
	lengthField = lengthField + len("\x0D")
	formattedLength = "0" + str(lengthField)

	code = header + filetype + iin + version + jurVer + entries + subType + formattedOffset + formattedLength + subType + "DAQ" + licNum + "\x0ADCS" + formattedlastName + "\x0ADDEN\x0ADAC" + formattedfirstName + "\x0ADDFN\x0ADAD" + formattedmiddleName + "\x0ADDGN\x0ADCA" + classif + "\x0ADBA" + expire + "\x0ADBD" + issue + "\x0ADBB" + dob + "\x0ADBC" + genderFormated + "\x0ADAY" + eyes + "\x0ADAZ" + hairs + "\x0ADAU" + height + "\x0ADAG" + street + "\x0ADAI" + city + "\x0ADAJ" + state + "\x0ADAK" + zip + "\x0ADCGUSA\x0ADCF" + discriminator + "\x0ADCJ" + audit + "\x0ADCK" + inventory + "\x0ADDA" + compliance + "\x0ADDB" + revision

	if (FlagRestriction):
		code = code + "\x0ADCB" + restriction
	if (FlagEndosernent):
		code = code + "\x0ADCD" + endorsenet
	
	if veteran:
		code = code + "\x0ADDL" + '1'
	if (organDonor):
		code = code + "\x0ADDK" + '1'

	return code


lastName = input("Input first name: ")
middleName = input("Input middle name: ")
lastName = input("Input last name: ")
gender = input("Input a gender (m/f): ")
state = input("Input state (from table): ")
iin = input("Input IIN (from table): ")
street = input("Input street: ")
city = input("Input city: ")
zip = input("Input zip: ")
dob = input("Input DOB: ")
expire = input("Input expire date: ")
issue = input("Input issue date: ")
licNum = input("Input license num: ")
classif = input("Input classification: ")
revision = input("Input revision date: ")
restriction = input("Input restriction (Optional): ")
endorsenet = input("Input endosernent (Optional): ")
discriminator = input("Input discriminator: ")
inventory = input("Input inventory num: ")
audit = input("Input audit num: ")
eyes = input("Input eyes color (from table): ")
hairs = input("Input hairs color (from table): ")
feet = input("Input height in feets: ")
in_ = input("Input height in in\'s: ")
weight = input("Input weight in lbs: ")
veteran1 = input("Veteran? (0/1): ")
organDonor1 = input("Organ Donor? (0/1): ")

if veteran1 == "1":
	veteran = True
else:
	veteran = False
if organDonor1 == "1":
	organDonor = True
else:
	organDonor = False

code = gen(lastName, middleName, firstName, gender, state, iin, street, city, zip, dob, expire, issue, licNum, classif, revision, restriction, endorsenet, discriminator, inventory, audit, eyes, hairs, feet, in_, weight, veteran, organDonor)
codes = encode(code, columns=12, security_level=4)
image = render_image(codes)
image.show()
