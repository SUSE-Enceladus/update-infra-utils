DESTDIR=
PREFIX=/usr
EXEC_NAME=enable-rmt-repos

exec_verSpec=$(shell rpm -q --specfile --qf '%{VERSION}' $(EXEC_NAME).spec)

tar-exec:
	mkdir -p "$(EXEC_NAME)-$(exec_verSpec)"
	cp enable-rmt-repos Makefile "$(EXEC_NAME)-$(exec_verSpec)"
	tar -cjf "$(EXEC_NAME)-$(exec_verSpec).tar.bz2" "$(EXEC_NAME)-$(exec_verSpec)"
	rm -rf "$(EXEC_NAME)-$(exec_verSpec)"

install-exec:
	install -d -m 755 "$(DESTDIR)"/usr/sbin
	install -m 744 enable-rmt-repos "$(DESTDIR)"/usr/sbin
