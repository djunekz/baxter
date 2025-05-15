PREFIX = ../usr/bin

all:
	@echo Run \'make install\' to install baxter

install:
	@chmod 755 baxter
	@cp baxter $(HOME)/$(PREFIX)

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/baxter
