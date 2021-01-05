cek_versi_python(){
	echo "Please wait.. checking Python version"
	echo "python3 --version"
	
	MIN_VER="3.5"
	NOW_VERSION=$(python3 --version 2>&1)
	
	echo "$NOW_VERSION"
	VERSION_REGEX="^Python\ ((3\.[^0-4])|(3\.[1-9][0-9]+)|([4-9]+\.\d+))(.*)$"

	if [[ $NOW_VERSION =~ $VERSION_REGEX ]]; then
	        echo "Python Ok"
	else
		echo "\\033[38;5;202m Your Python $NOW_VERSION Not Comatible with this application, Please update your Python with new version  "
		exit 1
	fi
}
cek_ffmpeg(){
	echo "Cek FFMPEG"
	echo "ffmpeg --version"
	
	HASIL=$(ffmpeg --version)
	HASIL_ERROR=$?
	
	echo "$HASIL"
	
	if [ $HASIL_ERROR = '0' ]; then
		echo "FFMPEG Ready.. "
	else
		echo "\\033[38;5;202m FFMPEG not found"
		
		exit 1
	fi
}
install_requirements(){
	echo "Install package Python for depedencies.. "
	echo "pip3 install -r requirements.txt"
	
	HASIL=$(pip install -r requirements.txt)
	HASIL_ERROR=$?
	
	echo "$HASIL"
	
	if [ $HASIL_ERROR = '0' ]; then
		echo "Package now installed.. "
	else
		echo "\\033[38;5;202m Failed installation"
		
		exit 1
	fi
}
cek_versi_python
cek_ffmpeg
install_requirements
