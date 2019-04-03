#!/bin/bash

for file in `ls ./new_flv_file`
do
ffmpeg -i ./new_flv_file/$file ./new_mp4_file/${file%.*}.mp4
done
