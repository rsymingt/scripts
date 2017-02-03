#!/bin/bash

#currentDir=$(pwd)
#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#cd $DIR
#cd ..
#cd projects/projecto_cplus
#./projecto
currentdir=$(pwd)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/../projects/projecto_cplus/
make clear
make projecto
cd $currentdir
$DIR/../projects/projecto_cplus/./projecto
