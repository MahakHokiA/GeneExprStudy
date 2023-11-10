# mylist = '245 736 986 45.98'
# # mylist1 = mylist.strip().split()
# mylist2 = mylist.replace('','..')
# for i in mylist2:
#     print(float(i))



def filter_n(inputfile_line_list):
    empty_list = []
    for line in inputfile_line_list:
        for item in line:
            if item != 'NA' and item != 'N':
                empty_list.append(line)
    return empty_list

with open ('./GeneExprStudy.txt', 'r') as infile:
    inputfile_lines_list = infile.readlines()
    header = inputfile_lines_list [0]
    inputlines = filter_n(inputfile_lines_list)
    # inputlines_no_header = inputlines.remove(inputlines[0])
   
 
    # for line in inputlines:
    #     if line == inputlines[0]:
    #         pass
    #     else:
    #         new_line = line.strip().split()
    #         kidney_list = [float(new_line[6]), float(new_line[11]), float(new_line[16])]
    #         liver_list = [new_line[3], new_line[8], new_line[13]]
    #         for kidney_expr in kidney_list:
    #             if kidney_expr <= -1.5:
    #                 print(kidney_expr)
                 



inputlines_srt = ' '.join([str(item) for item in inputlines])
with open ('./Gene_Expr_Study_Filtered.txt', 'w') as outfile:
    outfile.write(inputlines_srt)

