PREFIX = ../usr/bin

all:
	@echo Run \'make install\' to install baxter

termux:
	@chmod 755 baxter
	@cp baxter $(HOME)/$(PREFIX)

linux:
	@chmod 755 baxter
	@cp baxter $(HOME)/../$(PREFIX)

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/baxter
