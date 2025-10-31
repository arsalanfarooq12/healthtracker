#!/bin/sh

GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
BLUE="\033[0;34m"

mkdir user/

echo -e "${GREEN}Setting Up the Virtual Environment ...${RESET}"
python3 -m venv venv
source venv/bin/activate

echo "Installing Dependencies ..."
pip install flask matplotlib

clear

echo -e "${GREEN}Choose an option:${RESET}"
echo -e "1) ${YELLOW}Run the app${RESET}"
echo -e "2) ${BLUE}Return to venv console${RESET}"
echo -e "${GREEN}"
read -p "Enter choice [1/2]:" choice
echo -e "${RESET}"
if [ "$choice" = "1" ]; then
	flask --app app run
elif [ "$choice" = "2" ]; then
	echo -e "${GREEN}Done Setting up${RESET}"
else
	echo -e "${RED}Invalid choice.${RESET}"
fi

 


