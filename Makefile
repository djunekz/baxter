PREFIX = /usr

all:
	@echo Run \'make install\' to install baxter

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p baxter $(DESTDIR)$(PREFIX)/bin/baxter
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/baxter

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/baxter
