f = open("/home/jared/insight/InsightCodingChallenge/input/itcont.txt")
header = f.readline().strip().split(',')
header[1:3] = [''.join(header[1:3])]
header[1] = 'name'
print('columns: ',header)
data = []
for l in f.readlines():
    entry = l.strip().split(',')
    entry[1:3] = [''.join(entry[1:3])]
    entry[-1] = float(entry[-1])
    data.append(entry)
f.close()

transpose = list(map(list, zip(*data)))
benedict = {}
for title, values in zip(header, transpose):
    benedict[title] = values

unique_drugs = sorted(list(set(benedict['drug_name'])))

drukqs = []
for i,drug in enumerate(unique_drugs):
    print(drug)
    prescribers = []
    sums = 0
    for j,element in enumerate(benedict['drug_name']):
        if drug == element:
            prescribers.append(benedict['id'][j])
            sums += benedict['drug_cost'][j]
    drukqs.append([drug,len(set(prescribers)),sums])

drukqs = sorted(drukqs, key=lambda x: x[-1], reverse=True)

new_header = ['drug_name','num_prescriber','total_cost']
drukqs.insert(0,new_header)

with open('/home/jared/insight/InsightCodingChallenge/insight_testsuite/temp/output/file.txt', 'w') as F:
    for item in drukqs:
        F.writelines(",".join(map(str,item)))
        F.write("\n")
F.close()