PREFIX = ../usr/bin

all:
	@echo Run \'make install\' to install baxter

install:
	@chmod 755 baxter
	@cp baxter $(HOME)/$(PREFIX)
	@cd .. && rm -rf baxter

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/baxter
