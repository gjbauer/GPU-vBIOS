all: bin2text

catvbios:
	cc -o catvbios catvbios.c

bin2text:
	cc -o bin2text bin2text.c

modvbios:
	cc -o modvbios modvbios.c

clean:
	rm catvbios modvbios bin2text
