#!/usr/bin/env bash


if [ -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY exists.
fi


if [[ ! -e $dir ]]; then
    mkdir $dir
elif [[ ! -d $dir ]]; then
    echo "$dir already exists but is not a directory" 1>&2
fi
