import os

path = parameters["path"]

# Windows and linux slashes go in opposite directions.
# Uncomment the slash appropriate for your system.
systemslash= parameters["slash"]
#systemslash='/'

maxfiles = parameters["maxfiles"]
def get_list_of_files(inDirectory, container=[]):
   x=0
   try:
      for entry in os.listdir(inDirectory):
         entry = inDirectory+systemslash+entry
         if os.path.isdir(entry):
            get_list_of_files(entry,container)
         else:
            filesize = os.path.getsize(entry)
            fileandsize = (filesize, entry)
            container.append(fileandsize)
      return container
      # End for
   except:
      x=x+1
   # End try
# End def

Final_List_of_Files = get_list_of_files(path)
Final_List_of_Files.sort(reverse=True)

fileCount=0
for obj in Final_List_of_Files:
   context.logOutput("%12d - %s" % (obj[0], obj[1]))
   fileCount = fileCount + 1
   if fileCount >= maxfiles:
      break
# End for
