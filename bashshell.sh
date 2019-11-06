pushd ()                                          #the first line merely save the first argument in the variable dirname for readability reasons 
{                                                 #the second line of the function pushs the new directory onto the stack
    dirname=$1                                    #the third line's main purpose is to change to the new directory
    DIR_STACK="$dirname ${DIR_STACK:-$PWD' '}"   
    cd ${dirname:?"missing directory name."}
    echo "$DIR_STACK"
 }
 popd ()
 {
    DIR_STACK=${DIR_STACK#* }
    cd ${DIR_STACK%% *}
    echo "$PWD"
  }                                               #the last line merely prints the contents of the stack, with the implication that the leftmost directory is both the current directory and at the top of the stack
