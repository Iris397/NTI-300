pushd ()                                          #This line is for save the first argument in the variable dirname for readability reasons 
{                                                 #It is for push the new directory onto the stack
    dirname=$1                                    #The reason for third line is to change to the new directory
    DIR_STACK="$dirname ${DIR_STACK:-$PWD' '}"   
    cd ${dirname:?"missing directory name."}
    echo "$DIR_STACK"
 }
 popd ()
 {
    DIR_STACK=${DIR_STACK#* }
    cd ${DIR_STACK%% *}
    echo "$PWD"
  }                                                #This line prints the contents of the stack, with the implication that the leftmost directory is all the current directory and also the top of the stack
cut -f4 -d\| ablums
cut -f$(getfield $fieldname) -d\| albums
 who | cut -d' ' -f1
 mail $(who | cut -d' ' -f1)
