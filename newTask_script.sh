#!/usr/bin/env bash
echo "Enter file name:"
read file_nm
echo "#!/usr/bin/python3" > $file_nm
chmod u+x $file_nm
echo "File created"
vi $file_nm
