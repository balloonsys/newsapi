# Sample
for i in {19465..19473}; do
	FOLDER=$i
	rm -rf $FOLDER/*.jpg
	rm -rf $FOLDER/*.png
	curl -o $i/thumb.jpg 'http://XXX.com/'$i'/thumb.jpg' && echo $i'/thumb downloaded' &
	curl -o $i/medium.jpg 'http://XXX.com/'$i'/medium.jpg' && echo $i'/medium downloaded' &
	wait
done