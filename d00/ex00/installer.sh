#!/bin/bash
last_version=$(echo -e "Python 3.7.4\n")
current_version=$(python -V)

if [ "$current_version" = "$last_version" ]; then
	echo -e "Python is already installed, do you want to reinstall it ?"
	read -p "[yes | no]> "
	if [[ ($REPLY == "yes") || ($REPLY == "Yes") || ($REPLY == "YES") || ($REPLY == "y") || ($REPLY == "Y") ]]; then
		rm -rf ~/Users/$whoami/miniconda3
		echo "Python has been removed."
		cd ~/Users/$whoami
		curl -O 'https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh'
		bash ./Miniconda3-latest-MacOSX-x86_64.sh
		rm Miniconda3-latest-MacOSX-x86_64.sh 
		echo "export PATH=\$Users/$whoami/miniconda/bin:\$PATH" >> ~/.zshrc
		exec /bin/zsh
		echo "Python has been installed."
	else
		echo "exit."
	fi
else
	rm -rf ~/Users/$whoami/miniconda3
	cd ~/Users/$whoami
	curl -O 'https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh'
	bash ./Miniconda3-latest-MacOSX-x86_64.sh
	rm Miniconda3-latest-MacOSX-x86_64.sh
	echo "export PATH=\$/Users/$whoami/miniconda3/bin:\$PATH" >> ~/.zshrc
	exec /bin/zsh
	echo "Python has been installed."
fi