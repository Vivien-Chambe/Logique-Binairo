noir='\e[0;30m'
gris='\e[1;30m'
rougefonce='\e[0;31m'
rose='\e[1;31m'
vertfonce='\e[0;32m'
vertclair='\e[1;32m'
orange='\e[0;33m'
jaune='\e[1;33m'
bleufonce='\e[0;34m'
bleuclair='\e[1;34m'
violetfonce='\e[0;35m'
violetclair='\e[1;35m'
cyanfonce='\e[0;36m'
cyanclair='\e[1;36m'
grisclair='\e[0;37m'
blanc='\e[1;37m'
neutre='\e[0;m'

	echo "\e[1;32m Une solution pour n = 4 \e[0;m"
	../picosat-960/picosat dimacs_4.cnf	
	echo "\e[1;32m Une solution pour n = 6 \e[0;m"
	../picosat-960/picosat dimacs_6.cnf
	echo "\e[1;32m Une solution pour n = 8 \e[0;m"
	../picosat-960/picosat dimacs_8.cnf
	echo "\e[1;32m Une solution pour n = 10 \e[0;m"
	../picosat-960/picosat dimacs_10.cnf
	echo "\e[1;32m Une solution pour n = 12 \e[0;m"
	../picosat-960/picosat dimacs_12.cnf
	echo "\e[1;32m Une solution pour n = 14 \e[0;m"
	../picosat-960/picosat dimacs_14.cnf