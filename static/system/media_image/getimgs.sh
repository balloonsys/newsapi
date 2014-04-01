# Sample
for i in {19540..19544}; do
	FOLDER=$i
	mkdir $i
	rm -rf $FOLDER/*.jpg
	rm -rf $FOLDER/*.png
	curl -o $i/thumb.jpg 'http://static.3gcst.com/system/media_image/'$i'/thumb.jpg' && echo $i'/thumb downloaded' &
	curl -o $i/medium.jpg 'http://static.3gcst.com/system/media_image/'$i'/medium.jpg' && echo $i'/medium downloaded' &
	wait
done