import sqlFunc as sqf
import fileFunc as ff

file = sqf.search_for_file(dName='JP3-09.3 Close Air Support')
print(file[0])
ff.display_File(file[0][0])
